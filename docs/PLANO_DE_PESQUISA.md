# Plano de pesquisa

**Edição:** 0.1.0 — 02/11/2026. **Estado:** planejamento em elaboração, sujeito à revisão do responsável.  
[Voltar ao README](../README.md)

## 1. Tema e delimitação

Construção e avaliação de um índice experimental de desempenho administrativo das organizações da sociedade civil em parcerias com o governo federal. O estudo é nacional e transversal aos órgãos concedentes, com análise longitudinal do histórico público recuperável.

O ponto de partida são organizações e suas trajetórias, não somente nomes atuais de instrumentos. Convênios históricos com OSCs integram o universo principal. Termos de fomento, colaboração e outros instrumentos elegíveis serão identificados em grupos próprios, preservando diferenças de regime.

A inclusão operacional de cada grupo dependerá de critérios documentados e da cobertura das fontes. A ausência de uma organização em determinada base não prova ausência de parceria.

## 2. Problema de pesquisa

Informações administrativas fragmentadas, desfechos demorados, mudanças normativas e desigualdade na quantidade de observações dificultam comparações entre organizações. Um cadastro amplo pode conter poucos eventos temporalmente utilizáveis. Uma nota única pode ocultar tanto desempenho quanto falta de evidência.

**Pergunta principal:** como construir uma síntese explicável e reproduzível do desempenho administrativo observado de OSCs que preserve a comparabilidade entre regimes, períodos e níveis de experiência registrada?

**Pergunta complementar:** em que condições o índice e a trajetória conhecida das organizações acrescentam informação para prever um desfecho posterior, e qual extensão histórica oferece maior utilidade?

## 3. Objetivos

### Objetivo geral

Desenvolver e avaliar um índice longitudinal, explicável e reproduzível de desempenho administrativo de OSCs em parcerias federais, integrando fontes públicas e explicitando as diferenças de regime, contexto e disponibilidade da informação.

### Objetivos específicos

1. Inventariar fontes públicas e caracterizar sua cobertura real por período, instrumento, organização e variável.
2. Construir uma base de vinculação entre organizações, instrumentos e eventos, com proveniência.
3. Definir indicadores candidatos fundamentados em conceitos e obrigações aplicáveis, distinguindo responsabilidades da OSC e do concedente.
4. Avaliar alternativas de janela, normalização, ponderação, agregação e suficiência de observações.
5. Examinar estabilidade, cobertura, incerteza e diferenças entre grupos comparáveis.
6. Investigar a utilidade preditiva do índice e da trajetória, se houver informação temporal e desfechos adequados.
7. Disponibilizar métodos, decisões, limitações e resultados auditáveis, observando regras de publicação e proteção de dados.

## 4. Hipóteses de trabalho

As hipóteses orientam experimentos; não são conclusões.

| ID | Hipótese a investigar | Evidência necessária |
|---|---|---|
| H1 | A integração de fontes amplia a cobertura utilizável | Conciliação nacional, instrumentos únicos e auditoria de campos |
| H2 | Uma janela recente representa melhor mudanças de desempenho que a agregação de todo o estoque | Comparação de janelas, estabilidade e análise de trajetória |
| H3 | A consideração de regime e contexto melhora a comparabilidade | Diagnóstico por estratos e análise de sensibilidade |
| H4 | Características históricas acrescentam informação a um desfecho futuro | Comparação temporal controlada com e sem histórico |
| H5 | Ampliar o período de treinamento pode ajudar, mas não necessariamente de forma monotônica | Experimentos de 5 anos, 10 anos e histórico completo elegível |
| H6 | Tratar explicitamente pouca evidência reduz classificações excessivamente confiantes | Comparação de estimativas brutas e alternativas de incerteza/regularização |

A rejeição de uma hipótese ou a ausência de ganho será registrada. O projeto não presume superioridade do Portal, de cinco anos, de pesos aprendidos ou de redes neurais.

## 5. População e unidades

**População de interesse:** OSCs com parcerias federais identificáveis em fontes públicas, respeitando os critérios de inclusão e os limites de cobertura observada.

**Unidades distintas:**

- Organização: identidade institucional, estabelecimento e eventual agrupamento justificável.
- Instrumento: parceria individual identificada e conciliada entre fontes.
- Evento: mudança ou ocorrência documentada ao longo do instrumento.
- Organização-período: unidade candidata de cálculo do índice, por exemplo OSC-mês.
- Instrumento-data de previsão: unidade candidata para um experimento preditivo.

A unidade do modelo será escolhida em função do desfecho. Probabilidades por instrumento não serão automaticamente convertidas em uma nota da organização.

## 6. Escopo incluído e condicionado

### Incluído no planejamento

- Abrangência nacional entre órgãos federais.
- Convênios históricos, fomento e colaboração com OSCs.
- Investigação de contratos de repasse e regimes específicos quando houver organizações elegíveis.
- Histórico antigo, inclusive anos 2000, conforme disponibilidade e auditabilidade.
- Dados públicos com acesso legítimo e regras verificadas.
- Perspectiva administrativa: execução registrada, cumprimento de obrigações e prestação de contas.

### Inclusão condicionada

- Regimes específicos: manter estratos próprios; não aplicar automaticamente regras do MROSC.
- Instrumentos sem transferência financeira: eventual contexto institucional, sem denominadores financeiros incompatíveis.
- Dados de decisões e sanções: somente com vinculação, datas, semântica e finalidade definidas.
- Informações de metas e objeto: somente quando houver cobertura e interpretação comparáveis.

### Fora da primeira versão

- Bases internas ou autenticadas de uso restrito.
- Decisões automáticas de habilitação, seleção, impedimento ou sanção.
- Inferência de fraude a partir de pendência, ausência de informação ou julgamento ainda não concluído.
- Mensuração causal de impacto social.
- Abrangência completa de parcerias estaduais e municipais financiadas exclusivamente por esses entes.
- Implantação operacional no SiAGIR ou em outro sistema.
- Uso de LLMs, grafos ou deep learning como requisito obrigatório.

## 7. Contribuição esperada

A contribuição proposta está na combinação de um protocolo de integração e temporalidade, indicadores adaptados ao contexto de OSCs e validação transparente. Será situada por revisão bibliográfica; não se afirma que este seja o primeiro índice ou o primeiro uso de ML no tema.

A pesquisa poderá demonstrar que determinados componentes não são observáveis com os dados disponíveis. Esse diagnóstico é um resultado relevante, não uma falha a ser ocultada.

## 8. Desenho geral

Pesquisa aplicada, quantitativa e observacional, com análise documental das regras e estrutura longitudinal quando os eventos puderem ser reconstruídos. A etapa retrospectiva será identificada como tal. Alegações de previsão antecipada exigirão avaliação que respeite o que era conhecido em cada corte.

As bases serão avaliadas em três níveis de uso:

1. Descrição histórica.
2. Cálculo de indicadores em data de referência.
3. Modelagem preditiva com informação disponível à época.

Um registro pode ser adequado ao primeiro nível e inadequado aos demais.

## 9. Produtos previstos

- Inventário e contratos das fontes.
- Matriz nacional de cobertura e qualidade temporal.
- Base analítica versionada e dicionários.
- Fichas e protótipo do índice, com componentes e incerteza.
- Experimentos estatísticos e, se viáveis, modelos preditivos comparativos.
- Relatório técnico, visualizações e documentação de reprodução.
- Registro de limitações, resultados negativos e decisões.

Não há cronograma com datas finais aprovado. O [roadmap](ROADMAP.md) usa fases e critérios de aceite.

## 10. Decisões ainda necessárias

- Definição operacional de OSC para registros históricos e casos ambíguos.
- Unidade de organização: CNPJ completo, estabelecimento e relações com a raiz.
- Dimensões finais, indicadores, denominadores e mínimo de evidência.
- Regra de normalização, pesos e eventual classificação em faixas.
- Momento e horizonte de uma previsão, desfecho e tratamento de censura.
- Critério de publicidade de resultados individuais.
- Licença do material próprio, infraestrutura e armazenamento.

Estas decisões serão registradas em [Registro de decisões](REGISTRO_DE_DECISOES.md), evitando escolhas retrospectivas baseadas apenas no resultado mais favorável.
