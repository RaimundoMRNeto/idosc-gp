# Governança, qualidade e uso responsável

**Versão documental:** 0.2.0 — novembro de 2026.  
**Estado:** regras de trabalho para o desenvolvimento do projeto.

## 1. Limites de uso

O IDOSC-GP é experimental. Não deve ser apresentado como cadastro oficial de regularidade, instrumento de sanção, prova de fraude, certificação de qualidade ou medida de impacto social.

Resultados individuais, se produzidos no futuro, exigirão validação, contextualização e revisão antes de eventual divulgação. Não haverá recomendação de seleção ou exclusão automática de OSCs.

## 2. Publicação no GitHub

Podem ser versionados, após revisão:

- Código, documentação, configurações sem segredos e testes.
- Dicionários, definições de indicadores e manifestos publicáveis.
- Exemplos sintéticos claramente identificados.
- Resultados agregados que não exponham informação desnecessária.
- Relatórios de validação e limitações.

Não publicar automaticamente:

- Bases brutas, cópias integrais de sistemas ou exportações autenticadas.
- Credenciais, tokens, cookies, tickets e parâmetros de sessão.
- Dados pessoais de responsáveis, beneficiários ou trabalhadores sem necessidade e fundamento de uso.
- Arquivos internos do MDA, SiAGIR ou de outros projetos.
- Saídas de notebooks, logs ou imagens que revelem essas informações.
- Pontuações individuais não validadas.

O fato de uma fonte ser consultável publicamente não elimina a necessidade de avaliar finalidade, necessidade, termos e risco de redistribuição.

## 3. Licença

A licença de reutilização do código e da documentação **ainda será definida pelo responsável**. Não foi escolhida automaticamente na criação do repositório.

As fontes conservam seus próprios termos. Uma futura licença do projeto não substituirá a licença dos dados de terceiros. Publicidade do repositório e concessão de uma licença aberta são decisões diferentes.

## 4. Qualidade e rastreabilidade

Cada extração deverá registrar origem, parâmetros não secretos, referência temporal, coleta, formato, hash e versão. Toda transformação deverá possuir regra verificável.

Dimensões mínimas de qualidade:

- Completude.
- Unicidade.
- Validade.
- Consistência.
- Atualidade e latência.
- Integridade de vínculos.
- Comparabilidade entre fontes e períodos.
- Disponibilidade temporal para o uso pretendido.

Registros ambíguos serão preservados em área de revisão ou excluídos de um uso específico com motivo documentado. Não serão corrigidos silenciosamente.

## 5. Comparabilidade e equidade

A ausência de histórico, o pequeno porte ou a atuação em território vulnerável não devem gerar, por definição, uma nota ruim.

Antes de comparar organizações:

1. Verificar exposição, quantidade de observações e obrigações aplicáveis.
2. Examinar diferenças entre regime, setor, concedente e época.
3. Separar responsabilidade da OSC e do órgão público.
4. Avaliar cobertura, erro e incerteza por grupos com suporte suficiente.
5. Reconhecer quando os dados não permitem uma classificação.

Agrupamentos estatísticos podem ajudar, mas não eliminam automaticamente desigualdades ou vieses. Nenhuma técnica será rotulada como “justa” apenas por ter sido aplicada.

## 6. Revisão, correção e contestação

Toda versão de resultado deverá indicar data-base, método, limitações e canal de registro de erro. Correções deverão manter histórico e distinguir:

- Erro na fonte.
- Erro de vinculação.
- Erro de transformação.
- Erro de cálculo.
- Interpretação inadequada.
- Mudança metodológica deliberada.

Não substituir retroativamente um resultado sem registrar a revisão.

## 7. Trabalho com assistência de IA

Assistência de IA pode apoiar pesquisa, documentação, programação e revisão. As contribuições devem ser verificadas pelo responsável, especialmente fatos, referências, regras jurídicas, código e interpretação de resultados.

Não enviar informações restritas ou credenciais a ferramentas sem autorização. Não apresentar texto ou código gerado como evidência de execução. Registrar no diário o uso relevante de assistência automatizada e a revisão realizada.

## 8. Segurança prática

- Manter segredos fora do Git e configurar acesso por mecanismos apropriados.
- Revisar alterações e saídas antes de cada commit.
- Utilizar dados sintéticos nos testes sempre que possível.
- Reconhecer que `.gitignore` evita inclusões acidentais, mas não remove arquivos já versionados nem substitui revisão de segurança.
- Diante de exposição de credencial, interromper publicação, revogar/rotacionar e tratar o incidente; apagar apenas a linha não basta.
- Não contornar autenticação, limites ou restrições dos provedores.

## 9. Portas de aprovação

| Publicação ou uso | Evidência mínima |
|---|---|
| Adicionar uma fonte | Identificação, acesso legítimo, termos e finalidade |
| Publicar um indicador | Ficha, testes, denominador, cobertura e limites |
| Publicar uma nota agregada | Validação de componentes, agregação, sensibilidade e interpretação |
| Alegar capacidade preditiva | Desenho temporal, referência, teste preservado e resultados |
| Divulgar resultados individuais | Revisão específica de risco, contextualização e correção |
| Reutilizar em decisão administrativa | Avaliação própria, externa ao escopo acadêmico inicial |


## 10. Governança operacional da arquitetura híbrida

**Decisões adotadas, ainda não implementadas:** PostgreSQL + Parquet + DuckDB (D11), extração RFB direcionada (D12) e execuções iniciais sob demanda (D13). O GitHub público continua restrito aos artefatos revisados; Bronze, banco relacional, Parquet de uso interno e cópias de segurança não são publicações automáticas.

### 10.1 Contrato mínimo por fonte e por execução

Registrar por `run_id`: sistema de origem, canal e URL canônica, edição/referência do conjunto, coleta, termos, formato e esquema observado, hash SHA-256, parâmetros não secretos, contagens de entrada/saída, código e versões, testes e decisão de promoção. Hash atesta identidade do arquivo, **não** validade substantiva. A edição do dicionário precisa corresponder ao arquivo efetivamente lido.

### 10.2 Portas de promoção e reversão

1. Preservar arquivo original e manifesto em Bronze sem sobrescrever snapshots anteriores.
2. Carregar e verificar o lote isoladamente em staging.
3. Exigir integridade do arquivo, aderência ao contrato, validade de chaves e rastreabilidade; falhas críticas bloqueiam publicação.
4. Registrar diferenças de cobertura, campos ausentes e conflitos de fonte, com tratamento e incerteza explícitos.
5. Obter revisão humana antes de promover Silver ou publicar uma edição Gold.
6. Manter a versão anterior disponível e demonstrar idempotência, backup e restauração na implementação.

Indicadores graduais de completude e compatibilidade terão linha de base empírica antes de definir tolerâncias; não há percentuais arbitrários de aprovação nesta edição.

### 10.3 Temporalidade, minimização e autorização

A data do evento, a do registro/disponibilização, a da coleta e a de corte são categorias distintas. Uma situação cadastral observada hoje não será atribuída a datas anteriores sem evidência. A seleção dirigida da RFB registrará origem dos CNPJs candidatos e os não encontrados; dados pessoais de sócios não serão coletados por padrão.

Cada etapa da engenharia de dados terá avaliação e aprovação próprias antes de mudanças de ambiente, ingestão, commits e publicação. A aprovação da E0 **não** autoriza E1, periodicidade mensal, uso de serviços em nuvem, divulgação de índices individuais nem treinamento de modelo. A `main` permanece sem alteração de proteção por esta diretriz.

Relacionados: [arquitetura](ARQUITETURA_DADOS.md), [decisões](REGISTRO_DE_DECISOES.md), [roadmap](ROADMAP.md).
