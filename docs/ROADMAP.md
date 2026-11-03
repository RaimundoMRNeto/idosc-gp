# Roteiro de desenvolvimento e critérios de aceite

**Versão documental:** 0.1.0 — 02/11/2026.  
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
