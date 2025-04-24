import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib.ticker import FuncFormatter
import seaborn as sns


df = pd.read_csv('vendas_regiao.csv')

#faturamento por regiao
def formata_moeda(valor, pos):
    return f"R$ {valor:,.0f}"

ax = plt.gca()
ax.yaxis.set_major_formatter(FuncFormatter(formata_moeda))



df['faturamento'] = df['quantidade'] * df['preco_unitario']

faturamento_regiao = df.groupby('regiao')['faturamento'].sum()
df_faturamento = faturamento_regiao.reset_index()


ax = sns.barplot(data=df_faturamento, x='regiao', y='faturamento')

for container in ax.containers:
    ax.bar_label(container, labels=[formata_moeda(v, 0) for v in container.datavalues], padding=5)

plt.title('Faturamento por região')
plt.ylabel('R$')
plt.xlabel('Região')
plt.xticks(rotation=40)
plt.tight_layout()
plt.show()

#grafico de pizza
participacao_regiao = df.groupby('regiao')['faturamento'].sum()

valores = participacao_regiao
labels = participacao_regiao.index

plt.pie(
    valores,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90
)

plt.title('Participação das Regiões no Faturamento Total')
plt.axis('equal')
plt.tight_layout()
plt.show()





