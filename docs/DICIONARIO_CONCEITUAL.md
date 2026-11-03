# Dicionário conceitual inicial

**Versão documental:** 0.2.0 — novembro de 2026.  
**Estado:** convenções propostas. Os nomes abaixo não são afirmações sobre colunas existentes nas fontes.

## 1. Identificação e proveniência

| Campo proposto | Tipo conceitual | Significado e regra |
|---|---|---|
| `fonte_id` | Texto | Identificador da família de dados |
| `canal_id` | Texto | API, arquivo ou outro canal, sem fingir independência da origem |
| `registro_id_original` | Texto | Identificador tal como recebido |
| `instrumento_id` | Texto | Identificador harmonizado, criado por regra documentada |
| `osc_id` | Texto | Identidade organizacional conforme decisão de resolução de entidades |
| `cnpj_original` | Texto | Valor original preservado |
| `cnpj_normalizado` | Texto | Identificador de 14 posições, incluindo suporte alfanumérico; preservar zeros |
| `cnpj_raiz` | Texto | Raiz extraída segundo especificação e regra explícita |
| `estabelecimento_tipo` | Categoria | Matriz/filial, quando informado |
| `vinculo_confianca` | Categoria ou medida | Evidência e qualidade do vínculo entre fontes, sem substituição de revisão |
| `arquivo_hash` | Texto | Hash do conteúdo efetivamente utilizado |
| `execucao_id` | Texto | Rodada que produziu o registro |
| `versao_metodologia` | Texto | Versão das regras de cálculo |

CNPJ completo, raiz e OSC não serão tratados como conceitos idênticos. A regra de agregação de filiais ainda precisa ser decidida e testada.

## 2. Regime e instrumento

| Campo proposto | Significado |
|---|---|
| `modalidade_original` | Categoria exatamente como publicada |
| `modalidade_harmonizada` | Categoria analítica com correspondência documentada |
| `regime_juridico` | Regime aplicável, quando verificável |
| `regime_evidencia` | Norma, cláusula, metadado ou outra evidência utilizada |
| `regime_classificacao_status` | Confirmado, proposto, ambíguo ou não identificado |
| `concedente_id_original` | Órgão conforme a fonte |
| `concedente_harmonizado` | Identidade tratada sem apagar sucessões institucionais |
| `objeto_original` | Descrição textual, com revisão de necessidade e publicação |
| `situacao_original` | Situação administrativa recebida |
| `situacao_harmonizada` | Correspondência analítica, sem presumir equivalência jurídica |
| `situacao_evidencia` | Dicionário ou documento que sustenta a interpretação |

Termo de fomento, termo de colaboração, convênio histórico e regime específico não são apenas nomes intercambiáveis. A data isolada não decide o enquadramento.

## 3. Datas

| Campo proposto | Uso |
|---|---|
| `data_celebracao` | Caracterizar a coorte de formação |
| `data_inicio_vigencia` / `data_fim_vigencia` | Vigência conforme versão observada |
| `data_limite_pc` | Prazo efetivo de prestação de contas, quando verificável |
| `data_apresentacao_pc` | Entrega pela organização |
| `data_decisao_pc` | Decisão do concedente, separada da apresentação |
| `data_evento` | Ocorrência administrativa analisada |
| `data_registro` | Registro no sistema de origem |
| `data_disponibilizacao` | Momento em que a informação ficou acessível, se comprovável |
| `coletado_em` | Momento da extração, com fuso explícito |
| `data_corte` | Limite de informação da análise |
| `data_fim_acompanhamento` | Limite de observação de um desfecho |

Preservar precisão conhecida: data sem horário não será transformada em horário exato fictício. Timestamps serão registrados com fuso; datas civis manterão seu significado no sistema de origem.

## 4. Valores financeiros

Distinguir valor global, repasse pactuado, contrapartida, desembolso, pagamento, despesa comprovada, devolução e saldo. Os nomes nativos e suas definições precisam ser verificados.

Regras propostas:

- Usar representação decimal apropriada para dinheiro.
- Registrar moeda, unidade e caráter acumulado ou referente a fluxo.
- Não somar snapshots acumulados como se fossem parcelas.
- Se comparar valores ao longo de muitos anos, documentar deflator, referência e uso analítico.
- Não tratar repasses federais como receita total da organização.
- Não inferir execução física ou impacto a partir de gasto.

## 5. Indicador e previsão

| Campo proposto | Significado |
|---|---|
| `indicador_id` | Ficha conceitual correspondente |
| `periodo_inicio` / `periodo_fim` | Janela aplicada ao evento pertinente |
| `numerador` / `denominador` | Componentes auditáveis |
| `valor_indicador` | Resultado bruto, quando calculável |
| `valor_normalizado` | Resultado após transformação versionada |
| `cobertura` | Informação suficiente para interpretar o resultado |
| `estado_evidencia` | Aplicável, ausente, sem atividade, insuficiente etc. |
| `desfecho_id` | Definição do resultado futuro |
| `desfecho_valor` | Resultado observado, não inferido pela ausência |
| `desfecho_conhecido_em` | Data de conhecimento do resultado |
| `censura_status` | Acompanhamento incompleto ou evento ainda não observado |
| `probabilidade_predita` | Saída de modelo, distinta do índice descritivo |

## 6. Ausências não equivalentes

1. **Não informado:** campo ausente na fonte.
2. **Não aplicável:** obrigação não se aplica ao caso.
3. **Sem atividade elegível:** nenhuma ocorrência compõe o denominador.
4. **Evidência insuficiente:** existem registros, mas não permitem cálculo confiável.
5. **Em acompanhamento:** desfecho ainda não observável.
6. **Valor zero:** zero efetivamente observado e semanticamente válido.

O armazenamento físico será definido depois; o significado não pode ser perdido ao converter todos esses estados para zero.

## 7. Correspondência com campos nativos

A primeira implementação acrescentará um mapa contendo: fonte, tabela, campo nativo, definição oficial, transformação, campo conceitual, teste, período de validade e limitação.

Este documento não deve ser usado como contrato de API antes dessa etapa.

## 8. Metadados e distinções adicionais da arquitetura híbrida

| Campo conceitual proposto | Significado e restrição |
|---|---|
| `versao_fonte` | Edição ou referência específica do conjunto que deu origem ao registro |
| `referencia_fonte` | Data ou período descrito pela própria fonte, distinta da data de coleta |
| `hash_sha256` | Integridade do arquivo original efetivamente processado |
| `run_id` | Identificador estável da execução; relaciona entrada, testes e promoção |
| `decisao_promocao` | Estado, responsável e referência da revisão humana da rodada |
| `presenca_mapa_osc` | Presença/classificação observada no Mapa, segundo edição e regra específica; não é situação cadastral |
| `situacao_cadastral_rfb` | Estado da inscrição informado pela edição RFB; não prova condição histórica |
| `motivo_cnpj_candidato` | Evidência que levou o CNPJ à extração dirigida, como Mapa ou participante de parceria |
| `data_fato` | Data da ocorrência administrativa documentada |
| `versao_gold` | Identificador dos arquivos Parquet gerados de uma Silver e metodologia específicas |

Os nomes acima são **propostos**, não são colunas constatadas nas fontes nem tabelas efetivamente criadas. `run_id` poderá ser o identificador físico escolhido para `execucao_id`, após decisão do contrato. A `data_disponibilizacao` deve permanecer ausente quando não comprovável; não será preenchida com `coletado_em`.

Modelo relacional físico candidato, sujeito a testes em E1/E5: catálogos de fonte/execução; OSC e estabelecimento com vínculo documentado; instrumento e participantes com identificadores por sistema; eventos e snapshots; conflitos e produtos analíticos. **PostgreSQL** será a referência harmonizada; **Parquet** armazenará os produtos analíticos; **DuckDB** os consultará. A existência de uma raiz CNPJ comum não basta, por si, para declarar OSCs idênticas.

Relacionados: [arquitetura](ARQUITETURA_DADOS.md), [decisões](REGISTRO_DE_DECISOES.md), [inventário](INVENTARIO_FONTES.md).
