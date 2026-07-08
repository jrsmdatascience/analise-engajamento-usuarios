Análise de Engajamento de Usuários: Entendendo o Comportamento por Tipo de Plano

Contexto de Negócio & Objetivo
Em plataformas digitais e produtos de tecnologia (SaaS), compreender como os diferentes perfis de clientes interagem com o sistema é vital para estratégias de retenção e prevenção de cancelamentos (Churn). Este projeto analisa o comportamento de engajamento dos usuários divididos entre os planos Gratuito e Premium.

O objetivo principal é responder a uma dor real de Produto: Qual modelo de negócio apresenta maior intensidade de engajamento por tempo de tela e como isso impacta a percepção de valor do produto?

Tecnologias e Habilidades Utilizadas
- Python (Pandas): Modelagem de dados tabulares, engenharia de novas métricas (Features) e manipulação avançada de agregações.
- Engenharia de Dados (Unificação): Simulação de relacionamento de tabelas de bancos de dados através do método `.merge()` (`INNER JOIN`).
- Seaborn & Matplotlib: Criação de gráficos de barras corporativos e tratamento de padrões modernos de código de visualização.
- Análise Comportamental: Agrupamento e quebra de métricas temporais para decodificar padrões de usabilidade.

Hipótese Investigada
> Hipótese: Usuários do plano Premium, por pagarem pelo serviço, possuem um engajamento (ações/curtidas por minuto) significativamente maior do que os usuários do plano Gratuito?

Resultados e Insights Extraídos
Após a consolidação dos dados cadastrais com os logs semanais de uso e a criação da métrica de intensidade (`curtidas_por_minuto`), os dados revelaram um cenário contraintuitivo:

1. Paradoxo do Engajamento: O plano Gratuito apresentou uma média de curtidas por minuto superior (~0.36) à do plano Premium (~0.26).
2. Decodificação do Comportamento: Usuários do plano gratuito exibem um comportamento mais focado em microinterações rápidas. Em contrapartida, os usuários Premium passam mais tempo total na plataforma, indicando um consumo de conteúdo mais profundo e reflexivo, gerando menos cliques por minuto mas retendo mais tempo de tela.

Recomendação Estratégica (Business Acumen)
Para o Diretor de Produto, a análise indica que a métrica de "Cliques/Curtidas" isolada não dita o sucesso do plano Premium. Recomenda-se:
- Mudar o indicador-chave de sucesso (KPI) do time de produto de "Volume de Interações" para "Tempo de Retenção de Sessão".
- Desenvolver gatilhos de engajamento específicos para os usuários Premium que valorizem a profundidade do consumo e justifiquem a assinatura recorrente.

Estrutura do Repositório
- `analise_comportamento.py`: Script Python estruturado com o pipeline de ETL, cálculo de métricas e plotagem do gráfico corrigido.
- `README.md`: Documentação executiva para apresentação no portfólio.
