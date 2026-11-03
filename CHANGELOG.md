# Histórico de alterações

## 0.2.0 — 2026-11-02

Atualização **exclusivamente documental** da arquitetura e do plano de engenharia de dados (E0), sem implantação de infraestrutura ou ingestão.

### Decidido e documentado

- PostgreSQL como referência relacional Silver, Parquet como persistência Gold e DuckDB para análises.
- Arquivos originais versionados por snapshot na camada Bronze, fora do Git.
- Receita Federal por extração dirigida ao universo documentado de CNPJs.
- Execuções iniciais sob demanda, com `run_id`, validações e promoção revisada.
- Etapas E0–E8, contratos de proveniência, regras temporais, separação de responsabilidades das fontes e dependências de implementação.
- Registro das decisões D11–D13; P06 revisto e periodicidade mensal P02 mantida como hipótese.

### Sem alteração de escopo operacional

- Nenhum banco, serviço, script de coleta, pipeline, indicador ou modelo foi implementado.
- Nenhuma licença, automação, banco em nuvem ou regra de proteção da `main` foi aprovada por esta edição.
- Issues I01–I09 permanecem como backlog, sem encerramento automático.

## 0.1.0 — 2026-11-02

Edição documental inicial. A versão identifica a documentação, não um software de cálculo pronto.

### Adicionado

- README detalhado e plano de pesquisa.
- Metodologia proposta e matriz de indicadores candidatos.
- Inventário documental de fontes públicas e referências.
- Plano analítico com validação temporal e comparação de janelas históricas.
- Arquitetura de dados proposta e dicionário conceitual.
- Governança, roteiro, registro de decisões e diário.
- Modelos para fontes, indicadores e experimentos.
- Orientações de contribuição, citação e modelos de tarefa e pull request.
- Arquivos básicos de organização do repositório.

### Estado e limites

- Nenhuma base nacional foi integrada nesta edição.
- Nenhuma pontuação foi calculada.
- Nenhum modelo foi treinado ou validado.
- Não há pipeline, aplicativo, dashboard ou CI implementado.
- Licença de reutilização ainda não definida.
- O próximo marco é a auditoria nacional das fontes prioritárias.

Identificadores de commits e datas técnicas estão disponíveis no histórico do Git.
