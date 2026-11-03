# Plano analítico e de validação temporal

**Versão documental:** 0.1.0 — 02/11/2026.  
**Estado:** protocolo proposto. Nenhum modelo foi ajustado ou avaliado.

## 1. Duas perguntas diferentes

1. **Índice:** a síntese proposta representa, com estabilidade e limites claros, o desempenho administrativo observado?
2. **Previsão:** as informações disponíveis em uma data ajudam a estimar um desfecho futuro específico melhor que uma referência simples?

Treinar um algoritmo para reproduzir a fórmula do índice não constitui validação externa do índice. Uma nota descritiva e uma probabilidade predita deverão permanecer identificadas como produtos distintos.

## 2. Cinco horizontes que não devem ser confundidos

| Elemento | Significado | Diretriz inicial |
|---|---|---|
| Acervo histórico | Todos os registros recuperados e preservados com origem | Não descartar instrumentos antigos apenas por idade |
| Janela do índice | Período dos eventos elegíveis para cada indicador | Cinco anos como hipótese, comparada a alternativas |
| Janela de treinamento | Coortes de exemplos usadas para ajustar o modelo | Comparar janelas recentes e históricas |
| Histórico das características | Quanto do passado de cada OSC será resumido em uma previsão | Pode exceder a janela dos exemplos de treinamento, se disponível naquela data |
| Horizonte de previsão | Intervalo futuro em que o desfecho é observado | Definir após auditoria de datas e maturação |

A expressão “usar toda a base” não significa misturar indiscriminadamente linhas de épocas e regimes diferentes.

## 3. Definição do primeiro problema preditivo

Escolher **um** problema inicial, após auditar os dados. Candidatos:

- Apresentação da prestação de contas fora do prazo aplicável.
- Ocorrência futura de um tipo de pendência administrativa bem definido.
- Tempo até regularização de pendência ou até outro evento observável.

Para o primeiro candidato, por exemplo, deverão ser definidos o marco de previsão, o prazo efetivo, as alterações conhecidas nesse marco, o horizonte de acompanhamento, as exclusões e a responsabilidade da OSC. “Rejeição das contas” é outro problema, com processo de observação e atraso diferentes.

Não usar um rótulo genérico de “OSC problemática”. Fraude, corrupção, inadimplência, sanção e demora de análise não são conceitos intercambiáveis.

## 4. Reconstrução do que era conhecido

Cada exemplo deverá ter:

- Organização e instrumento identificados.
- Data de previsão ou corte.
- Características disponíveis até esse corte.
- Fonte e evidência da disponibilidade de cada característica.
- Desfecho, data de ocorrência e data de conhecimento.
- Final do acompanhamento e motivo de eventual censura.

**Exemplo sintético:** para prever em 31/12/2020, não se pode usar a situação final cadastrada em 2025 como característica de 2020. Tampouco se pode fingir que uma sanção publicada em 2022 já era conhecida no corte.

Em uma simulação de treinamento realizada em uma data histórica, só poderão entrar rótulos que já fossem conhecidos nessa data. Resultados observados depois podem compor a avaliação futura, mas não o ajuste anterior.

Uma data de coleta atual não prova quando o conteúdo se tornou público. Quando essa disponibilidade não puder ser reconstruída, registrar a limitação e restringir a análise; não anunciar validade preditiva histórica.

## 5. Maturação, censura e exposição

Instrumentos recentes podem não ter tido tempo de produzir o desfecho. Instrumentos antigos podem acumular mais tempo de fiscalização e de registro.

Tratamentos possíveis, a decidir por problema:

1. Coortes com acompanhamento suficiente para um horizonte fixo.
2. Modelos de tempo até evento, com censura explicitamente representada.
3. Análise retrospectiva limitada quando a reconstrução temporal for insuficiente.

“Sem desfecho observado” não é automaticamente uma classe negativa. A seleção de apenas casos já encerrados também pode introduzir viés e deverá ser avaliada.

## 6. Experimento sobre o valor do histórico

| Experimento | Exemplos usados no treinamento | Características | Pergunta |
|---|---|---|---|
| A | Coortes elegíveis dos cinco anos anteriores ao corte | Conjunto comum e temporalmente válido | Referência recente |
| B | Coortes elegíveis dos dez anos anteriores ao corte | Mesmo conjunto comum | Ampliar o período ajuda? |
| C | Todo o histórico elegível anterior ao corte | Mesmo conjunto comum, com regime e época tratados | Registros muito antigos acrescentam informação ou ruído? |
| D | Mesmas coortes recentes de A | Conjunto de A acrescido de resumos históricos disponíveis | A trajetória antiga ajuda sem misturar exemplos de todos os regimes? |

Antes dos experimentos, fixar a janela retrospectiva de cada característica do conjunto comum. A, B e C devem alterar somente a seleção temporal dos exemplos de treinamento, mantendo essas definições. D acrescentará características históricas explicitamente identificadas, sem mudar silenciosamente o conjunto básico.

Todas as alternativas serão comparadas nos **mesmos testes futuros**, com orçamento de ajuste e critérios equivalentes. Na comparação principal, manter o conjunto comum de campos para evitar confundir ganho temporal com ganho de atributos. Extensões usarão experimentos separados.

Ponderação por recência, treinamento separado por regime e modelos hierárquicos poderão ser testados posteriormente. Não serão adotados por pressuposto.

A inclusão de convênios de meados dos anos 2000 depende de compatibilidade semântica, qualidade, identificação e temporalidade, não apenas de existir uma linha no arquivo. Dados antigos inadequados à previsão ainda podem ser úteis à descrição histórica.

## 7. Divisão de desenvolvimento e teste

Proposta:

1. Separar coortes cronologicamente.
2. Ajustar modelos em períodos anteriores.
3. Selecionar configurações por validações sucessivas em períodos posteriores.
4. Preservar um período final, com desfechos suficientemente maduros, para avaliação única após as escolhas.
5. Documentar o que ficou de fora por indisponibilidade ou falta de acompanhamento.

Não definir agora anos fixos de teste sem conhecer a cobertura. O teste mais recente não é necessariamente elegível se seus resultados ainda não amadureceram.

Cuidados adicionais:

- Não dividir aleatoriamente linhas repetidas do mesmo instrumento entre treino e teste.
- Controlar sobreposição de janelas e resultados; usar separação temporal adicional quando necessário.
- Avaliar separadamente OSCs já observadas e OSCs não vistas no treinamento.
- Para OSCs recorrentes, a utilização de seu passado pode ser legítima; reutilizar informação futura não é.
- Ajustar imputação, codificação, normalização, seleção de atributos e reamostragem somente no treinamento.
- Não usar identificadores como atalho de memorização sem justificativa e avaliação.
- Considerar a dependência entre exemplos da mesma organização ao estimar incerteza.

## 8. Modelos e complexidade

Ordem proposta, condicionada ao tipo de resposta:

1. Referência ingênua: prevalência, regra simples ou histórico disponível.
2. Modelo estatístico interpretável, como regressão logística para resposta binária.
3. Modelo de árvores ou boosting apropriado a dados tabulares.
4. MLP ou outro método de deep learning, somente com justificativa e comparação controlada.
5. Modelo de sobrevivência, se o problema for tempo até evento.

Não há escolha definitiva de biblioteca, arquitetura ou hiperparâmetros. A quantidade efetiva de organizações, eventos e casos independentes importa mais que o total bruto de linhas. Redes neurais não são requisito para que o projeto seja científico ou contemporâneo.

Explicações de um modelo poderão ajudar a entender associações utilizadas na previsão; não demonstrarão causalidade.

## 9. Métricas e comparação

Para classificação binária, considerar:

- Prevalência do desfecho.
- Precisão e sensibilidade em limiares justificados.
- Curva precisão–revocação e área correspondente, sobretudo com evento raro.
- ROC-AUC como informação complementar, não único critério.
- Brier score ou outra medida probabilística e análise de calibração.
- Resultados por período, regime, porte, setor e grupos com suporte suficiente.
- Intervalos de incerteza e tamanho dos grupos.

Para tempo até evento, usar métricas compatíveis com censura e horizontes definidos. Não comparar números produzidos em amostras ou horizontes diferentes como se fossem equivalentes.

Não serão fixadas metas arbitrárias de acurácia antes de conhecer prevalência, referência e custo dos erros. O limiar operacional, se algum dia proposto, exigirá decisão separada da avaliação acadêmica.

## 10. Validação do índice descritivo

A validação incluirá:

- Coerência entre conceito, indicadores e responsabilidades.
- Sensibilidade a janelas de três, cinco e sete anos, quando viáveis.
- Sensibilidade a pesos, normalização, agregação e cobertura mínima.
- Estabilidade de componentes e ordenações, sem supor que estabilidade extrema seja sempre desejável.
- Evidência externa independente e posterior, quando possível.
- Comparação por regime e avaliação de organizações com poucas observações.
- Registro de casos em que a agregação oculta diferenças relevantes.

Pesos iguais poderão ser uma referência inicial, não uma justificativa definitiva. Importância de atributos em um algoritmo ou variância explicada por componentes principais não define, sozinha, a importância substantiva de uma dimensão.

## 11. Reprodutibilidade e decisão

Cada execução utilizará o [registro de experimento](templates/REGISTRO_EXPERIMENTO.md), com dados, cortes, versões, parâmetros, semente, métricas, exclusões e limitações.

**Porta de entrada para previsão:** desfecho definido, datas confiáveis, quantidade suficiente de eventos, população documentada e disponibilidade temporal reconstruível.

Se esses requisitos falharem, a entrega será a análise descritiva e o índice que os dados sustentarem, com a previsão mantida como agenda futura. Resultados negativos — inclusive ausência de ganho ao usar toda a história ou deep learning — serão documentados.

Referências: [bibliografia](REFERENCIAS.md), [metodologia](METODOLOGIA.md), [roadmap](ROADMAP.md).
