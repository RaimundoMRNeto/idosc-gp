# Indicadores candidatos

**Versão documental:** 0.1.0 — 02/11/2026.  
**Estado:** proposta para auditoria de viabilidade. Nenhum indicador foi calculado ou aprovado como componente definitivo do índice.

## 1. O que estamos tentando medir

O objeto é o **desempenho administrativo observável da OSC na gestão de suas parcerias federais**. A disponibilidade de uma variável não é motivo suficiente para transformá-la em pontuação.

Cada candidato precisa passar por quatro perguntas:

1. O conceito é pertinente ao objetivo do índice?
2. O evento e sua responsabilidade podem ser identificados?
3. O numerador e o denominador podem ser reproduzidos?
4. A interpretação é comparável entre organizações, períodos e regimes?

Resultados de uma parceria decorrem também da atuação do concedente, de terceiros e de condições externas. O índice não pode atribuir automaticamente todas as ocorrências à OSC.

## 2. Matriz inicial

As fontes abaixo são **candidatas**. A presença dos campos, a semântica e a cobertura histórica ainda serão verificadas.

| ID | Candidato | Medida a investigar | Regra temporal e denominador | Principal limitação |
|---|---|---|---|---|
| I01 | Tempestividade da apresentação da prestação de contas | Proporção de prestações de contas apresentadas no prazo aplicável | Obrigações com prazo vencido na janela e acompanhamento suficiente; usar prazo efetivo, inclusive alterações documentadas | Prazo pode estar ausente; diferenciar entrega pela OSC e análise pelo concedente |
| I02 | Resultado da análise da prestação de contas | Distribuição de decisões: aprovação, aprovação com ressalvas e rejeição, conforme categorias verificadas | Decisões emitidas na janela; identificar também a coorte das obrigações que lhes deram origem | Casos analisados podem ser uma seleção; demora de análise não é falha automática da OSC |
| I03 | Atendimento a diligências | Proporção de respostas tempestivas, quando existirem solicitação, prazo, resposta e responsável | Diligências exigíveis na janela; excluir as não aplicáveis e sem prazo verificável | Dados possivelmente não estruturados ou indisponíveis; não presumir ausência de resposta |
| I04 | Cumprimento de entregas ou metas pactuadas | Proporção de entregas verificadas em relação às exigíveis, com critérios de aceitação documentados | Metas cujo vencimento e avaliação sejam observáveis, respeitando alterações do plano | Objetos heterogêneos; execução financeira não substitui comprovação física nem impacto social |
| I05 | Tempestividade de obrigações de encerramento | Cumprimento de obrigações específicas de encerramento, se atribuíveis à OSC | Obrigações vencidas na janela; separar entrega, devolução exigível e análise | Nem todo saldo devolvido é perda ou falha; necessidade de classificação do motivo |
| I06 | Regularização de pendências atribuíveis à OSC | Tempo até regularização de um tipo de pendência previamente definido | Coortes de abertura de pendências com tempo de acompanhamento observável | Pendências abertas exigem tratamento de censura; categorias não equivalentes não devem ser somadas |

**Fontes prioritárias para o teste:** Transferegov, Portal da Transparência e suas documentações; ver [inventário](INVENTARIO_FONTES.md). A disponibilidade de informações de execução física, diligências e prazos não está confirmada em todo o universo.

## 3. Perfil contextual, não pontuação automática

| Informação | Uso recomendado | O que não concluir |
|---|---|---|
| Quantidade de instrumentos e anos de experiência | Caracterizar trajetória e suficiência de evidências | Mais instrumentos não significam melhor gestão |
| Valores pactuados, transferidos e executados | Caracterizar escala, exposição e complexidade, com conceitos separados | Maior volume de recursos não significa maior desempenho |
| Porte, natureza jurídica e área de atuação | Descrever a população e formar comparações justificadas | Não privilegiar organizações grandes por construção |
| Modalidade, regime e concedente | Estratificar e interpretar diferenças de procedimento | Não aplicar a regra de um regime a outro sem exame |
| Município de sede e território de execução | Contextualização territorial | A sede não identifica automaticamente o local do benefício |
| Tempo de análise pelo concedente | Medir contexto administrativo e possível atraso de observação | Não atribuir esse tempo à OSC |
| Idade da organização e cadastro atual | Identificação e contextualização com referência temporal | Cadastro atual não descreve necessariamente a situação passada |
| Cobertura e quantidade de dados | Informar confiança e limitações | Ausência de dados não equivale a mau desempenho |

O uso dessas características como preditores também depende de disponibilidade no momento da previsão e de análise de vieses. Não serão incluídas apenas porque aumentam alguma métrica.

## 4. Ocorrências e resultados externos

CEPIM, CEIS, CNEP e decisões do TCU poderão apoiar contexto ou validação externa, desde que exista vinculação confiável, definição do evento, vigência e marco temporal.

Regras propostas:

- Não equiparar cadastro de impedimentos, sanção, instauração de tomada de contas e decisão definitiva.
- Não atribuir à organização um registro que se refira apenas a pessoa física responsável.
- Não classificar ausência de ocorrência como prova de regularidade.
- Não usar um evento simultaneamente como parte da pontuação e como validação independente dessa mesma pontuação.
- Não usar como característica preditiva a própria informação que define o desfecho futuro.
- Considerar diferenças de fiscalização, registro e oportunidade de exposição ao evento.

## 5. Regras de cálculo a especificar antes da implementação

Para cada indicador, preencher a [ficha de indicador](templates/FICHA_INDICADOR.md), incluindo:

1. Definição substantiva e interpretação.
2. Unidade de análise, população elegível e exclusões.
3. Numerador e denominador, com exemplo sintético.
4. Evento que ancora a janela e datas necessárias.
5. Responsabilidade da OSC, do concedente ou compartilhada.
6. Fonte, campos nativos verificados e regras de transformação.
7. Tratamento de valores ausentes, não aplicáveis e evidência insuficiente.
8. Sentido da medida, normalização e regras de agregação.
9. Comparabilidade entre regimes e mudanças normativas.
10. Quantidade mínima de evidências, incerteza e testes.
11. Versão, decisão de inclusão e limitações.

A fórmula de tempestividade poderá ser uma razão entre obrigações cumpridas no prazo e obrigações elegíveis. Isso **não define ainda** quais registros são elegíveis, qual prazo prevalece ou como tratar impedimentos externos; essas regras precisam ser documentadas primeiro.

## 6. Sinais que não devem virar indicadores de qualidade por conveniência

- “Situação concluída” sem comprovação do que essa categoria significa em cada fonte.
- Total repassado ou total de instrumentos isoladamente.
- Percentual financeiro executado interpretado como impacto social.
- Número bruto de pendências sem considerar exposição e natureza.
- Ausência de certificação não exigível para aquela organização.
- Quantidade de informações voluntariamente preenchidas em cadastro.
- Origem parlamentar do recurso.
- Uma nota calculada por modelo sem um conceito e uma validação independentes.

## 7. Decisão ao final da auditoria

Cada candidato será classificado como **elegível**, **elegível com restrições**, **não mensurável com as fontes atuais** ou **rejeitado por inadequação conceitual**.

O produto inicial pode ser um perfil multidimensional sem nota agregada, caso os dados não sustentem uma síntese comparável. Reduzir o escopo nessa situação é um resultado metodológico válido.

Relacionados: [metodologia](METODOLOGIA.md), [plano analítico](PLANO_ANALITICO.md), [governança](GOVERNANCA_DADOS.md).
