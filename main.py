import matplotlib.pyplot as plt

# Criando as listas com dados dos alunos
nomes_alunos = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
notas_medias = [88, 92, 85, 90, 95]

# Criando o gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(nomes_alunos, notas_medias, color='skyblue', edgecolor='navy', alpha=0.7)

# Adicionando título e rótulos
plt.title('Notas Médias dos Alunos', fontsize=16, fontweight='bold')
plt.xlabel('Nomes dos Alunos', fontsize=12)
plt.ylabel('Notas Médias', fontsize=12)

# Adicionando grade para melhor legibilidade
plt.grid(axis='y', alpha=0.3, linestyle='--')

# Definindo limites do eixo Y
plt.ylim(0, 100)

# Exibindo o gráfico
plt.tight_layout()
plt.show()
