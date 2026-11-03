# Diário de execução

## E001 — estruturação inicial do projeto

**Data de referência:** 02/11/2026, America/Sao_Paulo.  
**Responsável pelo projeto:** Raimundo de Moura Rolim Neto.  
**Atividade:** criação do repositório e elaboração da documentação inicial com assistência de IA.  
**Estado:** entrega documental inicial; implementação analítica não iniciada.

### Objetivo

Transformar a discussão sobre um índice de OSCs em um projeto versionado, com escopo, método proposto, fontes, prioridades, critérios de aceite e registro de pendências.

### Entradas

- Discussão de objetivos e abrangência nacional.
- Necessidade de preservar a trajetória de convênios anteriores ao MROSC.
- Hipótese de janela recente para o índice e histórico ampliado para experimentos.
- Documentação oficial e referências metodológicas listadas no repositório.
- Autorização do responsável para criar um repositório público.

### Procedimento

1. Criar o repositório público com a branch `main`.
2. Organizar os documentos por finalidade.
3. Separar decisões, propostas e resultados ainda inexistentes.
4. Revisar o planejamento e as fontes documentais.
5. Publicar os arquivos em commit identificável.
6. Conferir o conteúdo remoto e os vínculos internos.

O histórico do Git fornece os identificadores e horários dos commits. Não há necessidade de inserir o próprio hash do commit dentro dele.

### Entregas desta edição

- README detalhado e plano de pesquisa.
- Metodologia, candidatos a indicadores e plano analítico.
- Inventário de fontes e referências.
- Arquitetura proposta e dicionário conceitual.
- Governança, roteiro, decisões e modelos de registro.
- Orientações de contribuição e arquivos de organização do repositório.

### O que não foi realizado

- Download e integração das bases nacionais.
- Reprodução de contagens exploratórias mencionadas em discussões anteriores.
- Confirmação de cobertura completa ou de todos os endpoints.
- Cálculo de indicadores, pesos ou pontuações.
- Treinamento ou avaliação de machine learning/deep learning.
- Implementação de pipeline, aplicação, dashboard ou integração ao SiAGIR.
- Publicação de bases brutas ou resultados individuais.
- Definição de licença aberta.

### Limitações

A conferência inicial é documental. Fontes identificadas ainda precisam de auditoria empírica. A documentação constitui proposta de trabalho e deve ser revisada pelo responsável antes de sustentar decisões de pesquisa ou divulgação.

### Próxima execução

F1: auditar fontes P1 e produzir a matriz nacional de cobertura, chaves, campos e datas. Antes de calcular a nota ou escolher um algoritmo, verificar quais perguntas os dados realmente permitem responder.

## E002 — aprovação e formalização documental da arquitetura E0

**Data de referência:** novembro de 2026, America/Sao_Paulo.  
**Responsável pelo projeto:** Raimundo de Moura Rolim Neto.  
**Atividade:** registrar as decisões D11–D13 e alinhar arquitetura, governança, fontes, dicionário e roteiro por etapas.  
**Estado:** entrega documental; E1 e ingestões não iniciadas.

### Entradas e decisões

- Aprovação explícita de PostgreSQL + Parquet + DuckDB para a arquitetura híbrida.
- Aprovação da extração direcionada da Receita Federal, com universo de CNPJs documentado.
- Aprovação de execuções iniciais sob demanda.
- Aprovação da E0 para diagnóstico e formalização documental, sem autorização para E1.
- Documentação 0.1.0 e issues I01–I09 do repositório, preservadas como base.

### Procedimento e resultado

1. Examinar os documentos e o backlog existentes para evitar duplicações e conflitos.
2. Formalizar decisões e limites, distinguindo estado decidido de implementado/validado.
3. Especificar camadas Bronze/Silver/Gold, papel relacional do PostgreSQL e função analítica de Parquet/DuckDB.
4. Descrever vínculo entre MapaOSC, participantes de parcerias e extração dirigida da RFB.
5. Mapear E0–E8 às fases científicas e estabelecer aprovação humana antes de cada etapa.
6. Atualizar arquivos exclusivamente documentais no Git, com diff e identificação pelo histórico do commit.

### O que não foi realizado

Não foram instalados PostgreSQL, Python, DuckDB ou contêineres, criadas tabelas e credenciais, baixadas bases, implementados pipelines, calculados indicadores ou treinados modelos. A consulta aos materiais e as decisões de arquitetura não representam validação empírica de cobertura ou qualidade das fontes.

### Pendências

Capacidade de armazenamento e backup; versões exatas das ferramentas; contratos empíricos de dados; termos de uso por arquivo; escolha de coorte piloto; licença; autorização independente para E1. O histórico Git da presente alteração documental fornece o identificador do commit, sem introduzir um hash circular no documento.

## Modelo para novas entradas

### E000 — título da atividade

- **Data e fuso:**
- **Responsável:**
- **Objetivo:**
- **Estado:**
- **Decisão ou tarefa relacionada:**
- **Entradas e versões:**
- **Procedimento executado:**
- **Evidências e commit:**
- **Resultados observados:**
- **Testes realizados:**
- **Falhas e limitações:**
- **Uso de assistência automatizada e revisão:**
- **Próxima ação:**

Registrar atividades realizadas, não converter intenções do roadmap em fatos concluídos.
