# Roteiro de desenvolvimento e critérios de aceite

**Versão documental:** 0.2.0 — novembro de 2026.  
**Planejamento por entregas:** não há prazo acadêmico confirmado neste repositório.

## 1. Situação inicial

A edição 0.1.0 estabelece a documentação e a organização do trabalho. A ingestão nacional, a conciliação, os indicadores e os modelos ainda não foram executados.

| Fase | Entrega | Estado inicial | Condição para avançar |
|---|---|---|---|
| F0 | Repositório e documentação inicial | Entrega desta edição | Documentos publicados, referências e limites explícitos |
| F1 | Auditoria de fontes e cobertura | Planejada | Relatório reproduzível de cobertura, chaves, datas e elegibilidade |
| F2 | Base harmonizada e temporal | Planejada | Vínculos, conflitos, testes e manifestos verificáveis |
| F3 | Protótipo do perfil e dos indicadores | Planejada | Fichas, denominadores, regras de ausência e cálculo testado |
| F4 | Validação do índice | Planejada | Sensibilidade, comparabilidade, incerteza e revisão substantiva |
| F5 | Experimento preditivo | Condicional | Disponibilidade temporal e desfechos sustentam previsão |
| F6 | Relatório acadêmico e entrega reproduzível | Planejada | Evidências, limitações, versões e instruções suficientes |

A fase F5 pode não ser viável. Isso não invalida as contribuições de integração, descrição e construção do índice.

## 2. F1 — primeira prioridade

Tarefas:

- Definir operacionalmente a população de OSCs e os casos ambíguos.
- Auditar Portal da Transparência, Transferegov, MapaOSC e CNPJ.
- Verificar acesso, termos, dicionários e versões.
- Medir registros, instrumentos únicos e organizações por fonte e período.
- Conciliar interseções e registros exclusivos sem dupla contagem.
- Auditar modalidade, regime, datas, valores e desfechos.
- Distinguir informação atual e histórico reconstruível.
- Classificar elegibilidade para descrição, índice e previsão.

**Aceite:** outro leitor consegue reproduzir contagens e compreender exclusões, conflitos e limitações. Não é necessário que toda lacuna tenha solução.

## 3. F2 — integração

Tarefas:

- Implementar obtenção e preservação das entradas.
- Resolver identidade de instrumentos e OSCs.
- Manter modalidade original e evidência do regime.
- Construir eventos e snapshots conforme os dados permitirem.
- Implementar testes e relatório de qualidade.

**Aceite:** as principais transformações são reproduzíveis, nenhum conflito é ocultado e cada saída aponta para sua origem. Campos sem evidência não são preenchidos por suposição.

## 4. F3 e F4 — indicadores e índice

Tarefas:

- Selecionar candidatos viáveis.
- Preencher fichas e justificar exclusões.
- Criar exemplos sintéticos e testes de cálculo.
- Comparar janelas e escolhas de agregação.
- Examinar organizações com pouca informação.
- Definir apresentação de cobertura e incerteza.
- Submeter conceitos e resultados à revisão do responsável.

**Aceite:** cada componente é interpretável e auditável; a nota agregada só é publicada se houver sustentação. Um perfil sem ranking é alternativa legítima.

## 5. F5 — previsão, se viável

Tarefas:

- Escolher um desfecho, marco e horizonte.
- Reconstruir características e rótulos disponíveis por corte.
- Definir coortes, maturação, censura e teste final.
- Comparar referências simples, modelos tabulares e eventual MLP.
- Executar experimentos A–D do [plano analítico](PLANO_ANALITICO.md).
- Registrar resultados favoráveis e desfavoráveis.

**Aceite:** comparação temporal válida, sem vazamento, com métricas adequadas, calibração e limites. Não basta obter boa acurácia em divisão aleatória.

## 6. F6 — entrega

Conteúdo previsto:

- Relatório com pergunta, população, fontes, método, resultados e limitações.
- Código e ambiente reproduzível.
- Dicionário de dados e regras de conciliação.
- Versões dos indicadores e fichas.
- Manifestos e evidências publicáveis.
- Conclusões compatíveis com os testes realmente executados.

## 7. Primeiro backlog

| ID | Tarefa | Prioridade | Dependência | Produto esperado |
|---|---|---|---|---|
| T01 | Delimitar regras de identificação de OSC | Alta | F0 | Protocolo de inclusão e ambiguidades |
| T02 | Auditar fontes P1 e respectivos modelos | Alta | F0 | Fichas e matriz de disponibilidade |
| T03 | Definir coleta e armazenamento reproduzíveis | Alta | T02 | Configuração, manifesto e teste inicial |
| T04 | Medir cobertura nacional e sobreposição | Alta | T01–T03 | Relatório de cobertura |
| T05 | Definir matriz temporal por indicador | Alta | T02–T04 | Elegibilidade de campos e eventos |
| T06 | Aprovar indicadores e critérios mínimos | Alta | T05 | Fichas revisadas |
| T07 | Decidir licença do projeto | Média | Responsável | Decisão e arquivo de licença, se aprovado |
| T08 | Formalizar protocolo preditivo | Condicional | T04–T06 | Desfecho, coortes e testes |
| T09 | Revisar literatura e contribuição científica | Média | F0 | Síntese crítica com referências verificadas |

Esses itens são um backlog documental; não correspondem a issues já abertas automaticamente.

## 8. Regra de continuidade

Antes de iniciar uma fase, revisar o [diário](DIARIO_DE_EXECUCAO.md), o [registro de decisões](REGISTRO_DE_DECISOES.md) e as limitações da etapa anterior. Uma mudança de objetivo, população ou desfecho precisa de decisão explícita, não de adaptação silenciosa durante o experimento.

## 9. Etapas de engenharia de dados E0–E8

As etapas **E0–E8** detalham o caminho operacional e não substituem as fases científicas F0–F6. Uma etapa não passa automaticamente à seguinte. As diretrizes D11–D13 estão decididas; as implementações correspondentes permanecem sujeitas aos seus critérios de aceite.

| Etapa | Produto principal | Correspondência | Porta de aceite |
|---|---|---|---|
| **E0** — diagnóstico e formalização | Decisões, arquitetura e contratos documentais | F0/F1; T01–T03 | Revisão dos documentos e aprovação da publicação; nenhuma infraestrutura |
| **E1** — ambiente mínimo | PostgreSQL isolado, Python/SQL, Parquet/DuckDB, manifesto e backup testado com dados sintéticos | F1/F2; T03; [I04](https://github.com/RaimundoMRNeto/idosc-gp/issues/4) | Reprodutibilidade, isolamento e restauração |
| **E2** — MapaOSC Bronze | Snapshot preservado, leitura, contrato e perfil de qualidade | F1; [I07](https://github.com/RaimundoMRNeto/idosc-gp/issues/7) | Contagens e divergências reproduzíveis |
| **E3** — parcerias e CNPJs candidatos | Auditoria de canais, beneficiários, universo dirigido e sobreposições | F1; [I05](https://github.com/RaimundoMRNeto/idosc-gp/issues/5), [I06](https://github.com/RaimundoMRNeto/idosc-gp/issues/6) | Chaves, cobertura e origem dos candidatos explícitas |
| **E4** — RFB dirigida | Filtragem dos registros oficiais de interesse, conciliação cadastral | F1/F2; [I01](https://github.com/RaimundoMRNeto/idosc-gp/issues/1), [I07](https://github.com/RaimundoMRNeto/idosc-gp/issues/7) | Solicitados, encontrados, ausentes, volume e divergências rastreados |
| **E5** — Silver relacional | Entidades, vínculos, instrumentos, eventos, snapshots e conflitos | F2; [I08](https://github.com/RaimundoMRNeto/idosc-gp/issues/8), [I09](https://github.com/RaimundoMRNeto/idosc-gp/issues/9) | Integridade PK/FK, deduplicação verificada e cobertura histórica |
| **E6** — Gold e perfil | Parquet versionado, indicadores candidatos, denominadores e relatórios DuckDB | F3; T05–T06 | Paridade Silver/Gold, qualidade temporal e fichas de indicadores |
| **E7** — análise científica condicional | Viabilidade do índice; eventual protocolo preditivo com corte temporal | F4/F5; T06/T08 | Validação substantiva; modelos só se houver rótulos e dados adequados |
| **E8** — entrega | Reprodução aprovada, relatório e material publicável | F6; T07/T09 | Fontes, métodos, resultados e limites auditáveis |

**Ordem necessária:** a extração RFB da E4 só é dirigida depois que E2 e E3 fornecerem a lista de CNPJs. E5 depende da auditoria dessas fontes; E6 não antecipa uma nota agregada; E7 pode concluir pela inviabilidade de previsão sem invalidar o projeto. Nenhuma etapa exige nuvem ou orquestrador distribuído no piloto.

**Fluxo de trabalho por etapa:** diagnóstico → proposta específica → autorização → execução → relatório de testes e limitações → avaliação humana → autorização de commit/PR, quando pertinente → deliberação da próxima etapa. A aprovação da E0 é **documental**. A E1 continua **não iniciada e não autorizada**.

Relacionados: [decisões](REGISTRO_DE_DECISOES.md), [arquitetura](ARQUITETURA_DADOS.md), [governança](GOVERNANCA_DADOS.md).
