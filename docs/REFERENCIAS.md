# Referências e fontes de consulta

**Edição documental:** 02/11/2026.  
Os links abaixo sustentam o planejamento. Sua inclusão não significa que bases completas tenham sido baixadas ou que todos os recursos de uma API tenham sido testados.

## 1. Normas e referência institucional

### R01 — Lei nº 13.019/2014, texto consolidado

[Câmara dos Deputados — norma atualizada](https://www2.camara.leg.br/legin/fed/lei/2014/lei-13019-31-julho-2014-779123-normaatualizada-pl.html).

Uso: conceitos de OSC e instrumentos, exceções, transição e vigência; atenção aos arts. 2º, 3º, 83 e 88. O ano de publicação da lei não deve ser usado isoladamente como data de substituição de todos os convênios. Registros históricos e situações específicas exigem enquadramento próprio.

### R02 — Decreto nº 8.726, de 27 de abril de 2016

[Planalto — texto oficial](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2016/decreto/d8726.htm).

Uso: regulamentação federal das parcerias sob o MROSC. Preservar versão consultada e alterações aplicáveis. Não aplicar retroativamente obrigações sem examinar o regime do instrumento.

### R03 — Manual metodológico IDTRU-DL, versão 2.0

[Transferegov — página do manual](https://www.gov.br/transferegov/pt-br/ferramentas-gestao/paineis-gerenciais/arquivos/manual-metodologico-idtru-dl-v2.0).

Uso: referência institucional para dimensões, eventos e recortes temporais de desempenho em transferências. A janela deve ser interpretada conforme a definição de cada indicador, não como filtro universal por celebração.

O IDOSC-GP não é implementação oficial do IDTRU. A adaptação à população de OSCs e às fontes disponíveis precisará de justificativa e validação próprias. Não confundir a data do documento com sua disponibilização ou republicação no portal.

## 2. Fontes de dados prioritárias

### R04 — Portal da Transparência

- [Convênios — arquivos](https://portaldatransparencia.gov.br/download-de-dados/convenios).
- [Convênios — dicionário](https://portaldatransparencia.gov.br/dicionario-de-dados/convenios).
- [Origem e atualização dos dados](https://portaldatransparencia.gov.br/origem-dos-dados).
- [Catálogo de downloads](https://portaldatransparencia.gov.br/download-de-dados/).

Uso: identificação, cobertura histórica e conciliação. A situação atual não equivale automaticamente a uma série histórica de estados.

### R05 — Transferegov

- [Arquivos CSV](https://api-publica.transferegov.gestao.gov.br/downloads).
- [Catálogo de APIs](https://api-publica.transferegov.gestao.gov.br/).
- [API Discricionárias e Legais](https://api-publica.transferegov.gestao.gov.br/discricionarias/docs).
- [API Gestão de Parcerias](https://api-publica.transferegov.gestao.gov.br/parcerias/docs).
- [Página oficial de apresentação e cronograma](https://www.gov.br/transferegov/pt-br/ferramentas-gestao/api-de-dados-abertos-transferegov.br).

Uso: registros e eventos do ciclo das parcerias conforme cobertura verificada. Diferenciar módulos, canais e sistemas de origem.

### R06 — Mapa das OSCs / Ipea

- [Bases, coleções e dicionários](https://mapaosc.ipea.gov.br/base-dados).
- [Código oficial de construção da base](https://github.com/Plataformas-Cidadania/mapa-osc-data-import).

Uso: classificação e caracterização institucional. Avaliar metodologia, atualização e informações de organizações baixadas; evitar viés de sobrevivência.

### R07 — Receita Federal / CNPJ

- [Dados abertos](https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/dados-abertos).
- [Metadados](https://www.gov.br/receitafederal/dados/cnpj-metadados.pdf/@@download/file).
- [CNPJ alfanumérico](https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/acoes-e-programas/programas-e-atividades/cnpj-alfanumerico).
- [Anexo técnico do formato](https://normas.receita.fazenda.gov.br/sijut2consulta/anexoOutros.action?idArquivoBinario=76204).

Uso: identificação cadastral e compatibilidade dos identificadores. A base atual não reconstrói, sozinha, atributos passados.

As demais fontes e suas restrições estão no [inventário](INVENTARIO_FONTES.md).

## 3. Construção e avaliação de índices

### R08 — OECD / European Union / Joint Research Centre (2008)

*Handbook on Constructing Composite Indicators: Methodology and User Guide.*

[Publicação oficial](https://www.oecd.org/en/publications/handbook-on-constructing-composite-indicators-methodology-and-user-guide_9789264043466-en.html).  
DOI: [10.1787/9789264043466-en](https://doi.org/10.1787/9789264043466-en).

Uso: estrutura conceitual, qualidade, normalização, ponderação, agregação e sensibilidade. Não oferece justificativa automática para pesos específicos do IDOSC-GP.

## 4. Aprendizado de máquina e temporalidade

### R09 — Kapoor, S.; Narayanan, A. (2023)

*Leakage and the reproducibility crisis in machine-learning-based science.* Patterns.

DOI: [10.1016/j.patter.2023.100804](https://doi.org/10.1016/j.patter.2023.100804).  
[Versão de acesso em repositório](https://arxiv.org/abs/2207.07048).

Uso: prevenção de vazamento, adequação do teste à pergunta de pesquisa e reprodutibilidade. Distinguir versão publicada e versões do preprint.

### R10 — Yao et al. (2022)

*Wild-Time: A Benchmark of in-the-Wild Distribution Shift over Time.*

[NeurIPS — publicação](https://proceedings.neurips.cc/paper_files/paper/2022/hash/43119db5d59f07cc08fca7ba6820179a-Abstract-Datasets_and_Benchmarks.html).

Uso: mudança de distribuição no tempo e avaliação em períodos posteriores. Os resultados quantitativos do artigo não podem ser transferidos diretamente para OSCs.

### R11 — Grinsztajn, L.; Oyallon, E.; Varoquaux, G. (2022)

*Why do tree-based models still outperform deep learning on typical tabular data?*

[NeurIPS — publicação](https://papers.nips.cc/paper_files/paper/2022/hash/0378c7692da36807bdec87ab043cdadc-Abstract.html).

Uso: motivar comparações empíricas com modelos tabulares. Não sustenta afirmação de superioridade universal de árvores ou inviabilidade de redes neurais.

### R12 — Documentação de validação e censura

- [scikit-learn — validação cruzada](https://scikit-learn.org/stable/modules/cross_validation.html).
- [scikit-survival — introdução](https://scikit-survival.readthedocs.io/en/stable/user_guide/00-introduction.html).

Uso: desenho de avaliação, tratamento de dados censurados e implementação futura. Quando houver código, fixar versões das bibliotecas e registrar a documentação correspondente.

## 5. Revisão de literatura a desenvolver

A bibliografia inicial não é uma revisão sistemática. A próxima etapa deverá registrar perguntas, bases de busca, termos, período, critérios de inclusão/exclusão e síntese crítica.

Temas prioritários:

- Medição de desempenho de organizações sem fins lucrativos.
- Transferências e parcerias com OSCs no Brasil.
- Indicadores compostos e comparação entre organizações heterogêneas.
- Desfechos administrativos, seletividade da fiscalização e atraso de observação.
- Validação temporal e aprendizado com registros administrativos.
- Incerteza, amostras pequenas, explicabilidade e uso responsável.

Não afirmar ineditismo apenas porque uma busca inicial não encontrou proposta idêntica.
