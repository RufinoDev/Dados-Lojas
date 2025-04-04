import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('Loja_data.csv')

print(dados.head())

print(dados.info())

print(dados.describe())

print(dados['Estado'].unique())

receita_por_estado = dados.groupby('Estado')['Receita (R$)'].sum()
print(receita_por_estado)

plt.figure(figsize=(10, 6))
plt.bar(receita_por_estado.index, receita_por_estado.values, color='skyblue')
plt.title('Receita Total por Estado', fontsize=16)
plt.xlabel('Estado', fontsize=12)
plt.ylabel('Receita (R$)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(dados['Receita (R$)'], bins=30, color='pink', edgecolor='black', alpha=0.7)
plt.title('Distribuição da Receita', fontsize=16)
plt.xlabel('Receita (R$)', fontsize=12)
plt.ylabel('Frequência', fontsize=12)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 8))
estado_proporcao = dados['Estado'].value_counts()
plt.pie(estado_proporcao, labels=estado_proporcao.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.viridis.colors[:len(estado_proporcao)])
plt.title('Proporção de Estados', fontsize=16)
plt.tight_layout()
plt.show()