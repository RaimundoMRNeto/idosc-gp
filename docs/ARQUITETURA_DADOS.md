# Arquitetura de dados proposta

**Versão documental:** 0.1.0 — 02/11/2026.  
**Estado:** desenho de referência; nenhuma infraestrutura ou rotina de ingestão foi implementada.

## 1. Princípio

Separar os dados recebidos, sua harmonização e os produtos analíticos. O resultado deve permitir voltar de uma pontuação até as transformações e registros que a originaram.

O acervo histórico completo não se confunde com a tabela usada em cada cálculo ou treinamento.

## 2. Camadas lógicas

| Camada | Conteúdo | Regras |
|---|---|---|
| Bruta | Arquivos e respostas originais obtidos legitimamente | Preservar conteúdo, URL, parâmetros não secretos, data, referência, hash e termos |
| Harmonizada | Entidades, instrumentos, eventos, vínculos e conflitos | Conservar valores originais; documentar conversões, correspondências e exclusões |
| Analítica | Observações elegíveis, indicadores por período e exemplos preditivos | Registrar cortes temporais, denominadores, versão e finalidade |
| Divulgação | Documentação, resultados agregados e evidências publicáveis | Revisar risco de identificação, interpretação e condições de redistribuição |

As expressões bronze, silver e gold poderão ser usadas como equivalentes das três primeiras camadas, sem exigir uma plataforma específica.

## 3. Entidades conceituais

- **Organização:** identidade da OSC e atributos com referência temporal.
- **Estabelecimento:** CNPJ completo e relação documentada com matriz/raiz.
- **Instrumento:** parceria identificada, modalidade, regime e partes.
- **Vínculo entre fontes:** correspondências e evidências de conciliação.
- **Evento:** ocorrência datada, tipo, responsável e fonte.
- **Snapshot:** estado observado de um registro em uma coleta.
- **Indicador por período:** componente, numerador, denominador, cobertura e resultado.
- **Exemplo preditivo:** corte, características disponíveis, desfecho e acompanhamento.
- **Execução:** dados, configurações, código, testes e resultados de uma rodada.

Essas entidades ainda não constituem um esquema físico. Ver o [dicionário conceitual](DICIONARIO_CONCEITUAL.md).

## 4. Identidade, duplicidade e conflito

Proposta de sequência:

1. Preservar identificadores nativos e fonte.
2. Validar CNPJ como texto, compatível com formato numérico e alfanumérico.
3. Vincular por chaves oficiais verificadas.
4. Examinar colisões, mudanças cadastrais e registros sem chave.
5. Usar correspondência aproximada apenas como hipótese revisável.
6. Registrar divergências em vez de sobrescrever silenciosamente.

O mesmo instrumento presente em dois portais não representa duas parcerias. Ordens bancárias, parcelas, metas e eventos associados também não aumentam a contagem de instrumentos únicos.

Não eleger uma fonte vencedora para todos os campos. Uma fonte pode oferecer maior cobertura histórica e outra maior detalhe de execução.

## 5. Temporalidade e rastreabilidade

Manter separadamente, quando disponíveis:

- Data do fato administrativo.
- Data de registro no sistema.
- Data de disponibilização pública.
- Data de coleta.
- Data de corte do cálculo.

Quando uma data não estiver disponível, registrar ausência e consequência analítica. Não copiar a data de coleta para preencher artificialmente a data do evento ou da publicação.

Estados históricos deverão ser preservados por snapshots ou eventos. Reprocessar uma coleta não pode substituir silenciosamente a evidência usada em uma edição anterior do índice.

## 6. Tecnologias candidatas

Uma implementação inicial enxuta poderá utilizar:

- Python para obtenção, validação e coordenação.
- SQL para transformação e conciliação.
- Parquet para tabelas analíticas.
- DuckDB para processamento local e consultas.
- Git para código, documentação, configurações e testes.
- Notebooks ou Quarto para análises e relatório, se adequados à entrega acadêmica.

Versões, dependências e ambiente serão fixados na primeira implementação. Não há instalação ou configuração pronta nesta edição. Orquestração distribuída, DataHub, serviços em nuvem e integração ao SiAGIR são opções futuras, não requisitos assumidos.

## 7. Organização futura do código

Pastas candidatas, a criar somente quando houver conteúdo real:

- `src/`: ingestão, harmonização, indicadores e modelos.
- `tests/`: testes unitários, integração e validação dos dados.
- `configs/`: parâmetros sem credenciais.
- `notebooks/`: exploração com saídas revisadas.
- `reports/`: relatórios publicáveis.
- `data/`: dados locais não versionados, conforme política.
- `metadata/`: manifestos e dicionários publicáveis.

A estrutura existente nesta edição é documental; não pressupõe que essas pastas ou aplicações já estejam implementadas.

## 8. Manifesto de execução

Cada rodada deverá registrar: identificador, commit do código, versão da metodologia, fontes e hashes, períodos, configuração, ambiente, contagens de entrada e saída, rejeições, testes e localização autorizada das evidências.

Hashes demonstram identidade do arquivo, não sua exatidão substantiva.

## 9. Testes previstos

- Unicidade das chaves e integridade dos relacionamentos.
- Validade dos identificadores e das datas.
- Coerência de conceitos financeiros e unidades.
- Contagens antes e depois de cada transformação.
- Regras de exclusão e conflitos reproduzíveis.
- Cálculo de indicadores em exemplos sintéticos.
- Ausência de informação posterior ao corte nas características.
- Reexecução de um cálculo com o mesmo conjunto de entradas.

Relacionados: [governança](GOVERNANCA_DADOS.md), [roadmap](ROADMAP.md), [inventário](INVENTARIO_FONTES.md).
