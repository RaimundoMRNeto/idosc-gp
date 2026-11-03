# Inventário inicial de fontes públicas

**Versão documental:** 0.1.0 — consulta documental em 02/11/2026.  
**Estado:** fontes identificadas e documentação consultada; ingestão nacional e avaliação empírica de cobertura ainda não executadas neste repositório.

## 1. Como interpretar este inventário

Este documento registra **possibilidades de uso**, não garante que todos os campos ou períodos estejam disponíveis. Um portal, uma API e um arquivo CSV podem publicar dados do mesmo sistema de origem; não são necessariamente fontes independentes.

A observação anterior de maior cobertura do Portal da Transparência no recorte MDA motiva a comparação nacional, mas não a resolve. Não publicamos aqui contagens históricas sem extrações, filtros e evidências reproduzíveis.

Prioridades:

- **P1:** auditar primeiro; necessário à identificação das OSCs e à conciliação das parcerias.
- **P2:** complementar após o núcleo; inclusão condicionada à qualidade e finalidade.
- **P3:** extensão especializada; pode permanecer fora da primeira versão.

## 2. Famílias e canais

| ID / prioridade | Família e responsável | Acesso oficial | Uso candidato | Pendência central |
|---|---|---|---|---|
| F01 / P1 | Portal da Transparência — Convênios / CGU e sistemas de origem | [Arquivos](https://portaldatransparencia.gov.br/download-de-dados/convenios), [dicionário](https://portaldatransparencia.gov.br/dicionario-de-dados/convenios), [origens](https://portaldatransparencia.gov.br/origem-dos-dados) | Cobertura histórica, identificação de instrumentos, valores e conciliação | Medir cobertura, origem, duplicidade e datas; extrato atual não equivale a histórico de estados |
| F02 / P1 | Transferegov — Discricionárias e Legais / MGI | [CSV](https://api-publica.transferegov.gestao.gov.br/downloads), [API](https://api-publica.transferegov.gestao.gov.br/discricionarias/docs) | Instrumentos, propostas, participantes e etapas, conforme recursos disponíveis | Conferir modelos, chaves, campos e equivalência dos canais; não presumir todos os módulos operacionais |
| F03 / P1 | Mapa das OSCs / Ipea | [Bases e dicionários](https://mapaosc.ipea.gov.br/base-dados), [código de construção](https://github.com/Plataformas-Cidadania/mapa-osc-data-import) | Identificação de organizações e características institucionais | Examinar regras de classificação, versões, vinculação e completude |
| F04 / P1 | CNPJ / Receita Federal | [Dados abertos](https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/dados-abertos), [metadados](https://www.gov.br/receitafederal/dados/cnpj-metadados.pdf/@@download/file) | Identificação cadastral, natureza jurídica e resolução de entidades | Cadastro atual versus histórico; matriz/filiais; formato alfanumérico |
| F05 / P2 | Transferegov — Gestão de Parcerias / MGI | [API](https://api-publica.transferegov.gestao.gov.br/parcerias/docs), [anúncio oficial](https://www.gov.br/transferegov/pt-br/ferramentas-gestao/api-de-dados-abertos-transferegov.br) | Complementar o núcleo conforme cobertura efetivamente verificada | Documentação dinâmica e endpoints precisam ser testados; anúncio não prova cobertura integral |
| F06 / P2 | Portal — recursos transferidos, execução e emendas | [Catálogo](https://portaldatransparencia.gov.br/download-de-dados/), [emendas](https://portaldatransparencia.gov.br/download-de-dados/emendas-parlamentares), [documentos](https://portaldatransparencia.gov.br/download-de-dados/emendas-parlamentares-documentos/) | Contexto financeiro e origem dos recursos | Distinguir empenho, liquidação, pagamento, desembolso e execução pela OSC |
| F07 / P2 | CEPIM / Portal da Transparência | [Arquivos](https://portaldatransparencia.gov.br/download-de-dados/cepim), [conceito](https://portaldatransparencia.gov.br/entenda-a-gestao-publica/cepim) | Contexto ou desfecho administrativo específico | Vigência e histórico; ausência não prova regularidade; não é rótulo de fraude |
| F08 / P2 | CEIS e CNEP / Portal da Transparência | [CEIS](https://portaldatransparencia.gov.br/download-de-dados/ceis), [CNEP](https://portaldatransparencia.gov.br/download-de-dados/cnep) | Sanções com natureza, alcance e datas preservados | São cadastros distintos; vinculação correta à entidade e interpretação jurídica |
| F09 / P2 | Decisões e jurisprudência / TCU | [Serviço](https://portal.tcu.gov.br/carta-de-servicos/transparencia/dados-abertos-do-tcu), [dados abertos](https://sites.tcu.gov.br/dados-abertos/) | Validação complementar e análise documental | Não foi confirmada tabela nacional completa de TCE diretamente vinculável a CNPJ/instrumento |
| F10 / P3 | CEBAS, CNEAS e qualificação OSCIP / órgãos responsáveis | [MDS](https://www.gov.br/mds/pt-br/acoes-e-programas/suas/entidades-de-assistencia-social), [MJ](https://www.gov.br/mj/pt-br/assuntos/seus-direitos/entidades-sociais/oscip-1), [MapaOSC](https://mapaosc.ipea.gov.br/base-dados) | Caracterizar subconjuntos específicos | Certificação não é exigível de toda OSC; verificar abrangência, vigência e formato |
| F11 / P2 | Contexto territorial / IBGE | [SIDRA](https://sidra.ibge.gov.br/) | Códigos, população e condições territoriais para contexto e estratificação | Sede não equivale ao território de execução; não transformar vulnerabilidade territorial em penalidade |

## 3. Observações documentais que orientam a auditoria

### 3.1 Portal da Transparência

A documentação distingue dados de convênios e ordens bancárias e identifica sistemas de origem. Valores acumulados e situações extraídas hoje não reconstruirão, por si, o estado de um instrumento em uma data passada.

O teste inicial deverá comparar **instrumentos únicos e organizações**, e não somente número de linhas. Contagens por ano de celebração, modalidade e origem ajudarão a identificar a contribuição histórica de cada fonte.

A inexistência de uma data-limite de prestação de contas em determinado extrato não autoriza calculá-la a partir de um prazo genérico. Uma derivação só poderá ser utilizada se houver regra aplicável e evidência suficiente, sendo identificada como derivada.

### 3.2 Transferegov

O catálogo diferencia os canais CSV, API de Discricionárias e Legais e API de Gestão de Parcerias. Os modelos oficiais foram localizados, mas os arquivos e esquemas ainda precisam de inspeção reproduzível:

- [Modelo CSV — Discricionárias e Legais](https://www.gov.br/transferegov/pt-br/ferramentas-gestao/paineis-gerenciais/arquivos/modelo-dados-csvs-discricionarias-e-legais.zip/@@display-file/file).
- [Modelo API — Discricionárias e Legais](https://www.gov.br/transferegov/pt-br/ferramentas-gestao/paineis-gerenciais/arquivos/modelo_dados_api-discricionarias.zip/@@display-file/file).
- [Modelo API — Gestão de Parcerias](https://www.gov.br/transferegov/pt-br/ferramentas-gestao/paineis-gerenciais/arquivos/modelo_dados_api_parcerias.zip/@@display-file/file).

A página oficial consultada anuncia implantação gradual da API de Discricionárias e Legais: atos preparatórios entre julho e outubro/2026; instrumentos entre novembro/2026 e fevereiro/2027; execução financeira entre março e junho/2027; obras entre julho e outubro/2027. Essas datas são **cronograma anunciado**, não confirmação de entrega.

Links de painéis deverão ser registrados em formato público canônico, sem parâmetros de sessão ou tickets de autenticação.

### 3.3 Mapa das OSCs

A página consultada informa uma base principal que inclui organizações ativas e baixadas, com informações de matriz/filial, CNAE secundária e data de fechamento. A coleção anunciada na consulta era de agosto/2026. Há conjuntos adicionais, como projetos e áreas de atuação, que exigem avaliação própria.

A frequência declarada de atualização não substitui a verificação da data do arquivo efetivamente baixado. Informações não preenchidas não devem gerar penalidade.

### 3.4 CNPJ: identificação compatível com o formato alfanumérico

Segundo a [documentação da Receita Federal](https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/acoes-e-programas/programas-e-atividades/cnpj-alfanumerico), o identificador mantém 14 posições; as 12 primeiras podem ser alfanuméricas e as duas finais correspondem à verificação numérica. O projeto deve acomodar também os CNPJs numéricos existentes.

Regras propostas:

- Armazenar como texto, preservando zeros e letras.
- Padronizar caixa e remover somente separadores conhecidos.
- Não converter para inteiro e não usar limpeza que elimine todas as letras.
- Validar os formatos conforme a especificação oficial, sem inventar dígitos faltantes.
- Preservar CNPJ completo e raiz em campos distintos.
- Não agregar estabelecimentos automaticamente sem uma decisão sobre a unidade organizacional.

## 4. Ficha mínima de cada fonte

Usar o [modelo de ficha](templates/FICHA_FONTE.md). Campos essenciais:

- Identificador, família, sistema de origem e órgão responsável.
- Canal, URL canônica e condições de acesso.
- Granularidade, chaves e dicionário de campos.
- Cobertura declarada e cobertura efetivamente observada.
- Data de consulta, referência do dado, extração e disponibilização, quando conhecidas.
- Frequência declarada e atualizações observadas.
- Licença ou termos de uso e restrições de redistribuição.
- Tamanho, formato, contagem e hash do arquivo efetivamente usado.
- Evidência de sobreposição com outras fontes.
- Estado de validação, limitações e próximo teste.

**Estados:** identificada → documentada → amostra inspecionada → ingestão reproduzida → qualidade avaliada → elegível por finalidade.

A finalidade deve ser indicada separadamente: descrição, cálculo de indicador ou previsão. Não existe aprovação única para todos os usos.

## 5. O que não integrar automaticamente

- SIAFI autenticado, Tesouro Gerencial, planilhas internas, exportações restritas ou dados fechados utilizados em outros projetos.
- Microdados identificáveis de emprego que não estejam efetivamente disponíveis para uso público nos termos necessários.
- Informações pessoais de responsáveis sem necessidade demonstrada.
- Bases estaduais e municipais tratadas como se a cobertura nacional estivesse completa.
- Dados de painéis sem definição de filtro, população e data de referência.
- Documentos sem confirmação de identidade da OSC ou vínculo com o instrumento.

O repositório público deve utilizar apenas fontes e usos compatíveis com sua autorização e finalidade.

## 6. Próxima execução proposta

1. Registrar versão e termos de acesso das quatro famílias P1.
2. Inspecionar dicionários e pequenas amostras, sem publicar dados identificáveis desnecessários.
3. Produzir contagens nacionais reproduzíveis por fonte, ano e modalidade.
4. Medir interseções, registros exclusivos e conflitos de identificação.
5. Auditar datas, desfechos, granularidade e disponibilidade histórica.
6. Emitir um relatório que selecione campos elegíveis para cada produto.

Relacionados: [arquitetura](ARQUITETURA_DADOS.md), [dicionário conceitual](DICIONARIO_CONCEITUAL.md), [referências](REFERENCIAS.md).
