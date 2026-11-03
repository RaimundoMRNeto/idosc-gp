# Registro de decisões

**Edição inicial:** 02/11/2026.

Este registro separa o que orienta o projeto das hipóteses que ainda precisam de teste. “Decidido” não significa “implementado” ou “validado”.

## 1. Vocabulário de estados

- **Decidido:** orientação de escopo assumida para o desenvolvimento.
- **Proposto:** alternativa a avaliar.
- **Em verificação:** existe trabalho de avaliação em andamento, com evidência a registrar.
- **Implementado:** há artefato executável ou documento efetivamente entregue.
- **Validado:** critérios de aceite específicos foram atendidos e documentados.
- **Substituído:** decisão anterior mantida no histórico, com referência à nova.

## 2. Orientações consolidadas

| ID | Decisão | Justificativa e consequência |
|---|---|---|
| D01 | Repositório público `RaimundoMRNeto/idosc-gp` | Versionar planejamento e execução; não publicar automaticamente dados brutos |
| D02 | Abrangência nacional de parcerias federais | A experiência no MDA motiva o estudo, mas não delimita a população nacional |
| D03 | Incluir a trajetória histórica de OSCs, inclusive convênios | Termos de fomento e colaboração não constituem filtro exclusivo |
| D04 | Preservar regime, modalidade original e evidência | Evitar equiparar instrumentos e obrigações de épocas diferentes |
| D05 | Preservar o histórico recuperável | A janela de cálculo não determina o que deve ser descartado do acervo |
| D06 | Separar perfil, índice e previsão | Uma síntese administrativa não é automaticamente uma probabilidade nem avaliação de integridade |
| D07 | Exigir rastreabilidade temporal na previsão | Não usar informação posterior como se estivesse disponível no passado |
| D08 | Desenvolvimento experimental e não punitivo | Não automatizar impedimento, sanção, seleção ou exclusão de OSCs |
| D09 | Manter resultados e limitações reproduzíveis | Documentar fontes, transformações, exclusões, testes e versões |
| D10 | Não escolher licença automaticamente | A publicidade do repositório foi autorizada; os termos de reutilização serão decididos separadamente |
| D11 | Arquitetura híbrida: PostgreSQL + Parquet + DuckDB | PostgreSQL mantém os dados relacionais harmonizados (Silver); Parquet armazena produtos analíticos versionados (Gold); DuckDB executa análises e verificações, sem substituir o banco relacional |
| D12 | Receita Federal: extração direcionada | Formar conjunto de CNPJs de interesse com origem documentada; filtrar e reter somente os registros necessários, após validar os meios oficiais de acesso e seu custo |
| D13 | Execuções iniciais sob demanda | Cada rodada será identificada, testada e submetida a revisão humana antes de promover uma versão; não há agendamento nem periodicidade automática aprovados |

O nome IDOSC-GP é um nome de trabalho. Não há alegação de registro de marca, exclusividade do nome ou reconhecimento institucional.

## 3. Propostas que precisam de avaliação

| ID | Proposta | Evidência necessária |
|---|---|---|
| P01 | Janela móvel de cinco anos para o índice | Sensibilidade e pertinência do evento que ancora cada componente |
| P02 | Atualização mensal do cálculo | Frequência, latência das fontes e custo de operação |
| P03 | Indicadores de tempestividade e resultados administrativos | Campos, denominadores, responsabilidade e comparabilidade |
| P04 | Comparar cinco anos, dez anos, todo o histórico e características históricas | Protocolo temporal e coortes elegíveis |
| P05 | Usar modelos tabulares e eventual MLP | Problema definido, amostra efetiva e comparação com referência |
| P06 | Direção tecnológica inicial, **substituída em parte pela decisão D11** | Python e SQL permanecem ferramentas candidatas de execução; versões, volume e ambiente físico ainda dependem de diagnóstico. A combinação PostgreSQL + Parquet + DuckDB já está decidida. |
| P07 | Agregar dimensões em uma nota | Validação dos componentes, pesos, cobertura e sensibilidade |

As propostas não devem ser citadas como achados.

## 4. Decisões ainda abertas

- Identificação operacional de OSC em registros históricos.
- Unidade organizacional: estabelecimento, raiz ou vínculo institucional documentado.
- Tratamento de modalidades e regimes específicos.
- Indicadores definitivos, normalização, pesos e regras de compensação.
- Quantidade mínima de observações e apresentação de incerteza.
- Data de corte, frequência e limites exatos das janelas.
- Desfecho, horizonte e finalidade de um modelo preditivo.
- Condições de publicação de resultados individuais.
- Licença do código e da documentação.
- Requisitos acadêmicos finais e cronograma confirmado.

## 5. Como registrar uma nova decisão

Usar um identificador sequencial e informar:

1. Data, responsável e estado.
2. Problema e contexto.
3. Alternativas consideradas.
4. Evidências e limitações.
5. Decisão e justificativa.
6. Consequências para dados, código e resultados.
7. Documentos e experimentos relacionados.
8. Decisão anterior substituída, se houver.

Aprovar uma implementação técnica não equivale a validar uma hipótese científica. Alterações de método que afetem resultados deverão receber nova versão e análise de impacto.

## 6. Registro da aprovação da engenharia de dados — E0

Em novembro de 2026, o responsável aprovou as diretrizes D11–D13 e a etapa **E0 — diagnóstico e formalização documental**. As decisões registram arquitetura e modo de trabalho, **não** constituem evidência de banco, importação ou pipeline implementados.

- A arquitetura da engenharia de dados usará o refinamento Bronze (originais imutáveis) → Silver (PostgreSQL relacional) → Gold (Parquet), com DuckDB para análise.
- A extração direcionada da RFB depende da identificação preliminar de CNPJs a partir do Mapa das OSCs e dos participantes de parcerias federais; o meio efetivo de obtenção deverá ser testado sem presumir endpoint por CNPJ.
- As rodadas iniciais serão disparadas manualmente com identificador `run_id`, manifesto, testes e aprovação de promoção. A hipótese P02 de frequência mensal **permanece em aberto**.
- Nenhuma decisão sobre janela do índice, pesos, ML, licença, localização física, backup ou automação pode ser deduzida de D11–D13.
- As etapas E1 e seguintes exigem autorização específica, conforme o [roadmap](ROADMAP.md).
