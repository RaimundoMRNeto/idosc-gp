# Arquitetura de dados proposta

**Versão documental:** 0.2.0 — novembro de 2026.  
**Estado:** tecnologias e estratégia de execução aprovadas como decisões de arquitetura; nenhuma infraestrutura ou rotina de ingestão foi implementada.

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

As denominações **Bronze, Silver e Gold** são adotadas para as três primeiras camadas. A arquitetura medalhão é um padrão de organização e refinamento; não pressupõe contratação de uma plataforma específica.

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

## 6. Tecnologias e armazenamento aprovados

As três decisões técnicas de arquitetura estão registradas como D11–D13 no [registro de decisões](REGISTRO_DE_DECISOES.md).

| Componente | Persistência e função | Limite |
|---|---|---|
| Bronze | Arquivos originais por lote e snapshot, armazenados em área persistente **fora do Git** | Guardar bytes recebidos, referência, hash SHA-256 e condições de uso; nunca substituir uma edição já usada |
| Staging | Área transitória de preparo por execução | Conversões, validações e rejeições não afetam a versão Silver publicada |
| **PostgreSQL — Silver** | Banco relacional específico do IDOSC-GP para entidade, estabelecimento, participante, instrumento, eventos, snapshots e metadados de proveniência | Integridade referencial, histórico de lotes, conflitos e transações de promoção |
| **Parquet — Gold** | Conjuntos analíticos versionados, com cortes temporais, denominadores e método | Deriváveis da Silver e das versões de código; não se confundir com dados brutos |
| **DuckDB — consulta** | Motor embutido para processamento de Parquet e consultas controladas ao PostgreSQL | Não será fonte mestre das entidades, nem substituto da rastreabilidade SQL |
| Python e SQL | Obtenção, validação, transformação e testes | Dependências e versões serão fixadas somente na etapa técnica aprovada |

A arquitetura não exige inicialmente Spark, Databricks, Delta Lake, Iceberg, Airflow, dbt, Superset, DataHub, PostGIS ou serviços de nuvem. Sua eventual inclusão requer justificativa, diagnóstico de custo e aprovação.

**Isolamento:** o PostgreSQL, os arquivos e os backups deverão pertencer ao IDOSC-GP, sem compartilhar bases internas do SiAGIR, GCRS ou dados autenticados de outros projetos. Localização física, capacidade do SSD, versões e política de retenção permanecem pendentes para a E1.

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


## 10. Desenho relacional inicial e papel das fontes

O modelo físico será validado e criado na E1/E5, não nesta atualização documental. As tabelas conceituais a verificar são:

| Domínio | Entidades candidatas | Condição |
|---|---|---|
| Catálogo e execução | `fonte`, `versao_fonte`, `arquivo_original`, `execucao`, `validacao` | Origem, parâmetros não secretos, hash, rodada, resultado e aprovação |
| Identidade | `osc_entidade`, `estabelecimento`, `vinculo_osc_estabelecimento`, `classificacao_evidencia` | CNPJ completo/raiz como texto, `osc_id` distinto e evidência temporal |
| Parcerias | `instrumento`, `identificador_instrumento_fonte`, `participacao_instrumento` | Chaves nativas preservadas; uma parceria em dois canais não gera automaticamente dois instrumentos |
| Eventos e snapshots | `evento_instrumento`, `snapshot_instrumento`, `snapshot_cadastral` | Data do fato diferente de publicação, coleta e corte; sem estado histórico inventado |
| Divergências | `conciliacao_candidata`, `conflito`, `exclusao_justificada` | Correspondências aproximadas sempre revisáveis; motivos de exclusão persistentes |
| Metadados analíticos | `produto_analitico`, `versao_indicador` | Identificar a edição Gold e sua população, janela, versão e critérios |

**Fontes por atributo:** Receita Federal é referência dos dados cadastrais que publica; Mapa das OSCs/Ipea fornece classificação e enriquecimentos derivados; Transferegov e Portal da Transparência fornecem evidências de instrumentos conforme cobertura. Não existe fonte vencedora universal. Presença no Mapa, classificação como OSC, situação cadastral e participação em parceria são conceitos diferentes.

**Receita Federal dirigida (D12):** primeiro formar o conjunto documentado de CNPJs/raízes de interesse a partir do Mapa e de participantes de parcerias; depois avaliar a leitura/varredura dos arquivos oficiais e reter os registros pertinentes. “Direcionada” não pressupõe um endpoint de consulta em lote por CNPJ e não autoriza contornar restrições. A leitura de tabelas envolvendo pessoas físicas exige avaliação específica de necessidade e fundamento.

## 11. Contrato da execução sob demanda (D13)

Cada execução terá `run_id`, fonte/edição, hashes, parâmetros não secretos, referência temporal, commit do código, versões de ferramentas, contagens de entrada/saída, testes, conflitos e parecer de revisão. Estados de referência: `iniciada` → `extraida` → `validada` → `em_revisao` → `promovida`; falhas/rejeições não modificam o conjunto vigente.

A carga Silver deverá ser transacional e idempotente; a publicação Gold indicará versão e origem, de modo que possa ser refeita e revertida sem perda de evidências. Até nova decisão, **não haverá agendamento automático**. A operação, a recuperação e os limites de qualidade serão testados apenas após autorização da E1.

Relacionados: [governança](GOVERNANCA_DADOS.md), [roteiro E0–E8](ROADMAP.md), [inventário de fontes](INVENTARIO_FONTES.md).
