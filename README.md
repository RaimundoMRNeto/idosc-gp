# IDOSC-GP

## Índice de Desempenho das Organizações da Sociedade Civil na Gestão de Parcerias Públicas

Projeto acadêmico de Ciência de Dados voltado à construção e à avaliação de um índice experimental de **desempenho administrativo observável de OSCs em parcerias com o governo federal**, com abrangência nacional, integração de fontes públicas e análise longitudinal.

**Situação:** planejamento e estruturação documental. Esta edição não entrega uma base nacional consolidada, pontuações de OSCs, modelos treinados ou um sistema em produção.

| Identificação | Informação |
|---|---|
| Responsável | Raimundo de Moura Rolim Neto |
| Contexto acadêmico | Projeto integrador — Pós-graduação em Ciência de Dados / UTFPR |
| Nome de trabalho | IDOSC-GP; denominação provisória |
| Abrangência | Parcerias federais com OSCs em todo o Brasil, sem restrição a um ministério |
| Edição documental inicial | 0.1.0 — 02/11/2026, referência America/Sao_Paulo |
| Repositório | [RaimundoMRNeto/idosc-gp](https://github.com/RaimundoMRNeto/idosc-gp) |

O vínculo acadêmico contextualiza o estudo; não significa aprovação institucional da metodologia. O projeto não constitui índice oficial do governo, da UTFPR, do TCU ou do Ipea e não substitui o IDTRU-DL.

## 1. Problema e motivação

As informações sobre parcerias estão distribuídas entre sistemas, períodos e regimes jurídicos. Um mesmo conjunto pode apresentar situação atual e valores acumulados sem permitir reconstruir tudo o que era conhecido em determinada data. Além disso, OSCs com pouca experiência registrada não são diretamente comparáveis a organizações com muitas parcerias.

A pesquisa busca responder: **como sintetizar o desempenho administrativo observado das OSCs de forma explicável, temporalmente coerente e reproduzível, preservando as diferenças entre instrumentos e a qualidade das evidências?**

O histórico de convênios integra a população principal do estudo. Termos de fomento e colaboração são grupos analíticos importantes, mas não constituem o único filtro de inclusão. A classificação das organizações e dos regimes será documentada e auditada.

A experiência de conciliação de bases em outros projetos motivou a atenção ao Portal da Transparência: foi relatada maior cobertura no recorte MDA. Esse achado localizado não demonstra superioridade ou completude nacional de uma fonte. A comparação nacional ainda será executada.

## 2. Objetivos

**Principal:** desenvolver e avaliar um índice longitudinal, explicável e reproduzível de desempenho administrativo das OSCs em parcerias federais, considerando regime, período, contexto e disponibilidade da informação.

**Complementar:** investigar se o índice e a trajetória institucional conhecidos em uma data ajudam a prever um desfecho posterior específico, comparando diferentes extensões do histórico de treinamento.

A etapa preditiva depende de uma auditoria favorável das datas, dos resultados e do acompanhamento. Um resultado sem ganho preditivo também será reportado.

## 3. Produtos analíticos distintos

| Produto planejado | Pergunta | Limite |
|---|---|---|
| Perfil institucional e histórico | Que organização é esta e qual trajetória está documentada? | Experiência e volume não são, por si, desempenho. |
| Índice e seus componentes | Como se comportaram dimensões delimitadas do desempenho administrativo? | Não mede automaticamente impacto social, integridade ou capacidade total. |
| Modelo preditivo experimental | Qual a probabilidade ou o tempo até um evento futuro definido? | Previsão não é causa, sanção nem decisão de elegibilidade. |

Nenhuma pontuação deve ser usada para bloquear automaticamente organizações, declarar fraude ou substituir análise humana.

## 4. Decisões temporais

- Preservar todo o histórico público recuperável, inclusive convênios antigos.
- Adotar **cinco anos como hipótese inicial** para a janela do índice, conforme o evento de cada indicador, e testar sua sensibilidade.
- Não limitar o acervo nem o treinamento automaticamente pela data de assinatura.
- Comparar treinamento recente, ampliado e histórico completo elegível.
- Separar o uso de instrumentos antigos como exemplos de treinamento de seu uso como características históricas da OSC.
- Preservar datas do fato, registro/disponibilização e coleta, quando observáveis.
- Não transformar um extrato atual de instrumento antigo em uma suposta fotografia do passado.

## 5. Caminho metodológico

1. Delimitar OSCs, instrumentos, regimes e finalidade de cada análise.
2. Inventariar, extrair e conciliar as fontes nacionais.
3. Auditar chaves, completude, semântica e disponibilidade temporal.
4. Construir fichas de indicadores e testar alternativas de agregação.
5. Avaliar cobertura, incerteza, sensibilidade e comparabilidade do índice.
6. Executar um experimento preditivo temporal, se houver dados adequados.
7. Publicar resultados reproduzíveis, limitações e registros de decisão.

O [roadmap](docs/ROADMAP.md) define entregas e critérios de aceite. Pesos, faixas classificatórias, mínimo de observações e desfecho preditivo ainda não foram fixados.

## 6. Fontes prioritárias

- [Portal da Transparência — Convênios](https://portaldatransparencia.gov.br/download-de-dados/convenios): cobertura e conciliação histórica.
- [Transferegov — dados públicos](https://api-publica.transferegov.gestao.gov.br/): instrumentos, propostas e eventos, conforme cobertura efetivamente auditada.
- [Mapa das OSCs / Ipea](https://mapaosc.ipea.gov.br/base-dados): identificação e contexto institucional.
- [Receita Federal — dados abertos](https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/dados-abertos): cadastro e resolução de entidades.

Fontes complementares incluem emendas, execução financeira, CEPIM, CEIS, CNEP, decisões do TCU, cadastros setoriais e contexto territorial do IBGE. Cada uso depende de cobertura, datas, termos de acesso e semântica. Ver [inventário](docs/INVENTARIO_FONTES.md).

## 7. Guia de leitura

| Documento | Finalidade |
|---|---|
| [Plano de pesquisa](docs/PLANO_DE_PESQUISA.md) | Problema, objetivos, hipóteses, escopo e contribuição esperada |
| [Metodologia](docs/METODOLOGIA.md) | População, temporalidade, construção e validação do índice |
| [Indicadores candidatos](docs/INDICADORES_CANDIDATOS.md) | Conceitos, elegibilidade e riscos de interpretação |
| [Inventário de fontes](docs/INVENTARIO_FONTES.md) | Fontes, canais, possibilidades e pendências de verificação |
| [Plano analítico](docs/PLANO_ANALITICO.md) | Experimentos estatísticos, ML e possível deep learning |
| [Arquitetura de dados](docs/ARQUITETURA_DADOS.md) | Camadas, tabelas, rastreabilidade e tecnologias candidatas |
| [Dicionário conceitual](docs/DICIONARIO_CONCEITUAL.md) | Entidades, campos propostos e regras de identidade |
| [Governança dos dados](docs/GOVERNANCA_DADOS.md) | Qualidade, proteção, publicação e reprodutibilidade |
| [Roadmap](docs/ROADMAP.md) | Fases, entregas e critérios de conclusão |
| [Registro de decisões](docs/REGISTRO_DE_DECISOES.md) | Decisões consolidadas, propostas e questões abertas |
| [Diário de execução](docs/DIARIO_DE_EXECUCAO.md) | O que foi realizado e quais evidências faltam |
| [Referências](docs/REFERENCIAS.md) | Normas, manuais e trabalhos metodológicos |
| [Contribuição](CONTRIBUTING.md) | Fluxo de trabalho, revisão e documentação de mudanças |
| [Histórico de alterações](CHANGELOG.md) | Evolução das versões documentais |
| [Modelos de registro](docs/templates/README.md) | Fichas reutilizáveis de fonte, indicador e experimento |

## 8. Como começar

Clone o repositório:

```bash
git clone https://github.com/RaimundoMRNeto/idosc-gp.git
cd idosc-gp
```

Leia o plano de pesquisa, as decisões e a fase F1 do roadmap. A próxima entrega técnica será a matriz nacional de cobertura e temporalidade. Ainda não há comando de ingestão, instalação de dependências ou treinamento implementado.

Os documentos Markdown são a fonte de verdade inicial do planejamento. A estrutura de código será criada à medida que os contratos de dados forem definidos.

## 9. Reprodutibilidade e publicação

Dados brutos, bancos locais, credenciais, informações pessoais desnecessárias e resultados individuais não revisados não devem ser enviados ao Git. A presença de uma informação em fonte pública não autoriza automaticamente sua republicação integral neste projeto.

As contagens exploratórias discutidas antes da criação do repositório não são apresentadas como resultados reproduzidos. Para publicação de qualquer número, serão exigidos fonte, data-base, manifestação de cobertura, código, configuração e evidência verificável.

A licença do material próprio será definida pelo autor; nenhuma licença aberta específica foi escolhida nesta inicialização. Os dados e documentos de terceiros conservam seus termos próprios. Ver [governança](docs/GOVERNANCA_DADOS.md).

## 10. Limites de interpretação

Este é um estudo experimental de desempenho administrativo registrado, não um cadastro oficial de risco, uma certificação de OSCs ou uma avaliação causal de impacto. Incerteza, lacunas e diferenças de contexto deverão acompanhar qualquer resultado.

A contribuição proposta é integrar **memória histórica ampla, avaliação recente contextualizada e validação temporal**. Sua utilidade será demonstrada por evidências, sem pressupor ineditismo, superioridade a índices existentes ou vantagem de um algoritmo específico.
