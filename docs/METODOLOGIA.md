# Metodologia de construção e avaliação do índice

**Estado:** protocolo proposto; parâmetros ainda não estimados.  
[Plano de pesquisa](PLANO_DE_PESQUISA.md) · [Indicadores candidatos](INDICADORES_CANDIDATOS.md)

## 1. Princípio central

O índice sintetizará dimensões delimitadas de desempenho administrativo observado. Capacidade institucional, contexto da parceria, qualidade da evidência e previsão futura deverão ser identificados separadamente.

A escolha de indicadores não deve ser determinada apenas pelos campos mais fáceis de obter. Cada componente precisa de uma relação explícita com o conceito medido e de evidência sobre a responsabilidade institucional.

## 2. Universo e identificação

1. Identificar instrumentos nas fontes públicas, preservando modalidade e códigos originais.
2. Vincular recebedores a identificadores institucionais e a classificações de OSC.
3. Registrar critérios de inclusão, exclusão e casos ambíguos.
4. Preservar organizações baixadas no acervo histórico quando relevantes para evitar seleção apenas das sobreviventes.
5. Não usar o rótulo atual “OSC” como único filtro de registros antigos.
6. Não presumir equivalência entre todas as entidades sem fins lucrativos e o universo jurídico/analítico definido para o estudo.

O cadastro atual não comprova a situação cadastral em uma data passada. Campos retrospectivos exigem fonte e evidência temporal próprias.

## 3. Regimes e modalidades

Convênios históricos e instrumentos do MROSC serão mantidos na pesquisa, com comparações por grupos justificáveis. A Lei nº 13.019/2014 distingue fomento, colaboração e cooperação e contém exceções e regras de transição; a entrada em vigor federal ocorreu em 2016, não no ano do número da lei. Ver [referências normativas](REFERENCIAS.md).

Campos mínimos: modalidade original, data de celebração, fundamento/regime identificado, origem da classificação e grau de confirmação.

Não classificar automaticamente todo convênio posterior a 2016 como erro. Não reclassificar um instrumento antigo como termo de fomento só porque uma decisão ocorreu depois da mudança normativa. Casos específicos serão revisados.

## 4. Conciliação de fontes

- Manter identificadores por sistema e uma chave analítica interna.
- Avaliar unicidade e estabilidade das chaves antes de juntar tabelas.
- Usar número do instrumento, processo, recebedor, concedente e datas como evidências de vinculação, sem assumir que um número isolado é globalmente único.
- Registrar correspondências confirmadas, prováveis e não resolvidas.
- Não somar registros duplicados nem valores acumulados de fontes sobrepostas.
- Preservar divergências e definir precedência por campo e finalidade; não substituir silenciosamente uma origem.
- Tratar CSV, API e painel do mesmo sistema como canais, não como observações independentes.

## 5. Temporalidade

### Cinco escolhas independentes

| Escolha | Regra inicial |
|---|---|
| Acervo | Todo o histórico recuperável |
| Janela do índice | Cinco anos como hipótese a testar |
| Janela de treinamento | Comparar 5, 10 anos e histórico completo elegível |
| Histórico das características | Comparar recente e acumulado |
| Horizonte de previsão | Pendente de definição do desfecho |

O recorte do índice deve seguir o evento pertinente. O manual do IDTRU-DL usa cinco anos da informação de cada indicador; serve de referência, não de fórmula automaticamente transferível às OSCs.

Para cada componente, documentar exatamente os limites inclusivos/exclusivos da janela e a regra para anos bissextos. A periodicidade mensal é uma proposta de trabalho; cada publicação deve registrar a data de referência e a data de disponibilidade da fonte.

### Eventos e estoques

- Um indicador de decisões recentes pode incluir instrumento antigo com decisão documentada na janela.
- Um indicador de obrigações vencidas precisa considerar a obrigação e seu prazo aplicável.
- Pendências ainda existentes devem permanecer visíveis como estoque atual, mesmo quando originadas antes da janela.
- A duração da análise do concedente não deve ser imputada integralmente à OSC.
- Uma decisão tardia não equivale, por si, a execução recente.

### Informações disponíveis no momento

Distinguir data do fato, data de registro/publicação, data de coleta e versão. Quando a disponibilidade histórica for desconhecida, registrar essa limitação. Não preencher retrospectivamente características com valores finais consultados hoje.

## 6. Indicadores

Cada indicador aprovado terá uma [ficha](templates/FICHA_INDICADOR.md) com:

- Conceito e dimensão.
- Unidade de análise.
- População elegível e responsabilidade institucional.
- Numerador e denominador.
- Evento temporal e janela.
- Variáveis, fontes, versões e transformações.
- Direção de interpretação e limites.
- Ausências, não aplicabilidade e suficiência de observações.
- Comparabilidade entre regimes.
- Testes, limitações e versão.

Devoluções, aditivos e complementações não são classificados automaticamente como falhas. Seus motivos e regras precisam ser examinados.

## 7. Normalização e agregação

O procedimento ainda será escolhido. As alternativas deverão preservar o significado dos componentes e ser comparadas em análises de sensibilidade.

Uma média ponderada de componentes em escala comum é uma referência experimental, não a fórmula aprovada. Pesos iguais podem servir de baseline, mas também representam uma escolha substantiva.

PCA, importância de variáveis e pesos otimizados não serão interpretados como “importância social objetiva”. Se pesos forem ajustados com um desfecho, isso configura uma tarefa supervisionada com seus próprios dados de treinamento e validação.

Deverão ser examinados:

- Redundância e correlação entre componentes.
- Compensação indevida de um resultado problemático por outro componente.
- Efeito de valores extremos.
- Dependência da pontuação em relação ao grupo usado para normalizar.
- Comparabilidade entre versões e ao longo do tempo.

Não recalibrar uma escala a cada período e interpretar toda mudança na nota como mudança real de desempenho sem decompor os efeitos.

## 8. Evidência insuficiente e incerteza

Separar explicitamente:

1. Ausência de informação.
2. Não aplicabilidade.
3. Ausência de atividade elegível.
4. Evidência insuficiente para estimar com precisão.
5. Resultado efetivamente observado.

Nenhuma dessas quatro primeiras condições equivale automaticamente a zero ou à melhor nota. Publicar denominadores e cobertura por componente.

Para pequenas amostras, avaliar intervalos de incerteza e, se pertinente, regularização hierárquica/agrupamento parcial. A alternativa deverá ter pressupostos, grupos de referência e efeitos examinados; não há garantia automática de equidade.

O limite mínimo de observações e as regras de divulgação serão definidos antes de produzir classificações finais.

## 9. Validação

### Conteúdo e coerência

Revisar se os indicadores representam o conceito, se a atribuição de responsabilidade é correta e se os componentes cobrem as dimensões pretendidas.

### Estrutura e sensibilidade

Comparar janelas de 3, 5 e 7 anos como cenários iniciais; pesos, normalização e agregação alternativos; retirada de componentes; disponibilidade por fonte e regime.

Avaliar mudanças de ordenação, estabilidade, cobertura e concentração de incerteza. Rankings não serão a única forma de apresentação.

### Validade externa

Quando possível, avaliar relação com desfechos posteriores e independentes. Não validar o índice apenas treinando um modelo para reproduzir sua fórmula.

### Análise entre grupos

Examinar diferenças por modalidade, regime, setor, porte observável, experiência e território. Características de contexto não devem funcionar automaticamente como penalidades.

## 10. Saída mínima por organização-período

- Identificação e período de referência.
- Componentes elegíveis e resultados.
- Denominadores e número de instrumentos.
- Cobertura das fontes e indicadores.
- Grau de incerteza/suficiência de evidências.
- Estratos e limitações relevantes.
- Versão da metodologia e das entradas.
- Pontuação agregada somente quando seus critérios forem atendidos.

Qualquer publicação individual depende de revisão e do protocolo em [Governança dos dados](GOVERNANCA_DADOS.md).

## 11. Condições para avançar

A primeira versão somente será calculada após a auditoria de dados e a definição das fichas mínimas. Ausência de datas ou desfechos pode levar à redução das dimensões, à publicação apenas de componentes ou à manutenção do estudo no nível descritivo. Essas mudanças serão registradas, não ocultadas.
