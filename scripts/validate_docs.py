#!/usr/bin/env python3
"""CI documental do IDOSC-GP, sem dependências de terceiros.

Verifica arquivos Markdown, links locais e presença de dados/segredos
indevidamente versionados. Não acessa links externos nem fontes de dados.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = (
    "README.md",
    "CONTRIBUTING.md",
    "docs/ARQUITETURA_DADOS.md",
    "docs/GOVERNANCA_DADOS.md",
    "docs/INVENTARIO_FONTES.md",
    "docs/REGISTRO_DE_DECISOES.md",
    "docs/ROADMAP.md",
)

DATA_SUFFIXES = {
    ".csv", ".tsv", ".xls", ".xlsx", ".xlsm", ".parquet",
    ".arrow", ".feather", ".duckdb", ".db", ".sqlite", ".sqlite3",
    ".zip", ".7z", ".tar", ".gz", ".pkl", ".joblib",
}
SECRET_SUFFIXES = {".pem", ".key", ".p12", ".pfx"}
SECRET_FILENAMES = {"id_rsa", "id_ed25519"}
FENCE = re.compile(r"^ {0,3}((?:\x60){3,}|~{3,})(.*)$")
LINK = re.compile(
    r"!?\[[^\]\n]+\]\(\s*(?P<dest><[^>]+>|[^\s)]+)"
    r"(?:\s+[\"'][^)]*[\"'])?\s*\)"
)
HEADING = re.compile(r"^#\s+\S")
SCHEME = re.compile(r"^[a-z][a-z0-9+.-]*:", flags=re.IGNORECASE)


def outside_fences(path: Path, content: str, errors: list[str]) -> list[tuple[int, str]]:
    """Devolve linhas de texto fora de blocos de código; verifica seu fechamento."""
    clean: list[tuple[int, str]] = []
    opened: tuple[str, int, int] | None = None
    for number, line in enumerate(content.splitlines(), start=1):
        marker = FENCE.match(line)
        if marker:
            token, remaining = marker.groups()
            if opened is None:
                opened = (token[0], len(token), number)
            elif token[0] == opened[0] and len(token) >= opened[1] and not remaining.strip():
                opened = None
            continue
        if opened is None:
            clean.append((number, line))

    if opened is not None:
        errors.append(f"{path.relative_to(ROOT)}:{opened[2]}: bloco de código não fechado")
    return clean


def check_link(path: Path, line_number: int, destination: str, errors: list[str]) -> bool:
    """Confere somente caminhos relativos do repositório; âncoras externas são ignoradas."""
    value = destination.strip().strip("<>")
    if not value or value.startswith(("#", "//")) or SCHEME.match(value):
        return False

    relative = unquote(urlsplit(value).path)
    if not relative:
        return False
    if relative.startswith("/"):
        errors.append(f"{path.relative_to(ROOT)}:{line_number}: link absoluto não verificável: {value}")
        return True

    target = (path.parent / relative).resolve()
    if not target.is_relative_to(ROOT):
        errors.append(f"{path.relative_to(ROOT)}:{line_number}: link sai do repositório: {value}")
    elif not target.exists():
        errors.append(f"{path.relative_to(ROOT)}:{line_number}: destino inexistente: {value}")
    return True


def check_markdown(path: Path, errors: list[str]) -> int:
    relative = path.relative_to(ROOT)
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeError:
        errors.append(f"{relative}: arquivo não está em UTF-8")
        return 0

    if not content.strip():
        errors.append(f"{relative}: documento vazio")
        return 0

    clean = outside_fences(path, content, errors)
    # Templates do GitHub têm campos/cabeçalhos próprios e podem não conter H1.
    if not relative.as_posix().startswith(".github/"):
        titles = [number for number, line in clean if HEADING.match(line)]
        if len(titles) != 1:
            errors.append(f"{relative}: esperado exatamente um título H1; encontrados {len(titles)}")

    links_checked = 0
    for number, line in clean:
        if line.startswith(("<<<<<<< ", ">>>>>>> ")):
            errors.append(f"{relative}:{number}: possível marcador de conflito de merge")
        for match in LINK.finditer(line):
            links_checked += int(check_link(path, number, match.group("dest"), errors))
    return links_checked


def tracked_paths(errors: list[str]) -> list[Path]:
    try:
        output = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT)
    except (OSError, subprocess.CalledProcessError) as exc:
        errors.append(f"não foi possível listar arquivos versionados: {exc}")
        return []

    return [Path(x.decode("utf-8")) for x in output.split(b"\0") if x]


def check_repository_hygiene(tracked: list[Path], errors: list[str]) -> None:
    for relative in tracked:
        name = relative.name.lower()
        if relative.suffix.lower() in DATA_SUFFIXES:
            errors.append(f"{relative}: dados, modelo ou arquivo compactado versionado; revisar política de armazenamento")
        if (
            relative.suffix.lower() in SECRET_SUFFIXES
            or name in SECRET_FILENAMES
            or name == ".env"
            or (name.startswith(".env.") and name != ".env.example")
        ):
            errors.append(f"{relative}: possível segredo/credencial versionado")


def main() -> int:
    errors: list[str] = []
    for required in REQUIRED:
        if not (ROOT / required).is_file():
            errors.append(f"documento obrigatório ausente: {required}")

    tracked = tracked_paths(errors)
    check_repository_hygiene(tracked, errors)

    markdown = sorted(ROOT / relative for relative in tracked if relative.suffix.lower() == ".md")
    if not markdown:
        errors.append("nenhum Markdown rastreado encontrado")

    link_count = sum(check_markdown(path, errors) for path in markdown if path.is_file())
    if errors:
        print(f"CI documental: {len(errors)} problema(s) encontrado(s):", file=sys.stderr)
        for issue in errors:
            print(f"  - {issue}", file=sys.stderr)
        return 1

    print(
        f"CI documental OK: {len(markdown)} Markdown, "
        f"{link_count} links relativos, {len(tracked)} arquivos rastreados."
    )
    print("Links externos e conteúdo das fontes não são validados por esta rotina.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
