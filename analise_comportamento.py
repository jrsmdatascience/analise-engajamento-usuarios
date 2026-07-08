# Analise engajamento de usuarios

import pandas as pd

# Bloco 1: Criando tabela do Perfil Cadastral dos Usuários
dados_usuarios = {
	'id_usuario': [101, 102, 103, 104, 105],
	'idade': [24, 42, 19, 35, 50],
	'plano': ['Gratuito', 'Premium', 'Gratuito', 'Premium', 'Premium']
}

df_usuarios = pd.DataFrame(dados_usuarios)
print('--- Tabela de Usuários ---')
print(df_usuarios)

# Bloco 2: Logs de Comportamento na Semana
dados_interacoes = {
	'id_usuario': [101, 102, 103, 104, 105],
	'minutos_uso': [30, 60, 15, 75, 122],
	'quantidade_curtidas': [10, 20, 6, 22, 35]
}

df_interacoes = pd.DataFrame(dados_interacoes)
print('\n--- Tabela de Interações ---')
print(df_interacoes)

# Bloco 3: Unificando as tabelas (O equivalente ao INNER JOIN do SQL)
df_comportamento = pd.merge(df_usuarios, df_interacoes, on='id_usuario', how='inner')
print(df_comportamento)

# Bloco 4: Engenharia de Features
df_comportamento['curtidas_por_minuto'] = df_comportamento['quantidade_curtidas'] / df_comportamento['minutos_uso']
print('\n--- Base com Nova Métrica ---')
print(df_comportamento)

# Quem interage de forma mais intensa por minuto na plataforma: os usuários do plano Gratuito ou os do Premium?

# Bloco 5: Análise Agrupada por Tipo de Plano
analise_plano = df_comportamento.groupby('plano')['curtidas_por_minuto'].mean().reset_index()
print('\n--- Média de Curtidas por Minuto por Plano ---')
print(analise_plano)

# ==========================================
# Bloco 6: VISUALIZAÇÃO GRÁFICA DO ENGAJAMENTO
# ==========================================

import matplotlib.pyplot as plt
import seaborn as sns

# configurando o estilo visual do gráfico
sns.set_theme(style='whitegrid')
plt.figure(figsize=(7, 5))

# criando o gráfico de barras
sns.barplot(
	data=analise_plano,
	x='plano',
	y='curtidas_por_minuto',
	hue='plano',
	legend=False,
	palette=['#3498db', '#2ecc71']
)

# adicionando títulos e rótulos explicativos
plt.title('Intensidade de Engajamento: Plano Gratuito vs. Premium', fontsize=13, pad=15, fontweight='bold')
plt.xlabel('Tipo de Plano contratado', fontsize=11)
plt.ylabel('Média de Curtidas por Minuto de Uso', fontsize=11)

# ajustando o layout para não cortar as margens e exibindo
plt.tight_layout()
plt.show()
