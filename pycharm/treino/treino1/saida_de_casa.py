# Forma de praticar meu python para data science
from random import randrange
import matplotlib.pyplot as plt # Importando biblioteca

meses_do_ano = ['Janeiro', 'Fevereiro', 'Março',
                'Abril', 'Maio', 'Junho', 
                'Julho', 'Agosto', 'Setembro', 
                'Outubro', 'Novembro', 'Dezembro']

# Lista para receber as vezes que poderei sair por mês
vezes_que_posso_sair = []

# Looping para quantia de mêses
for x in range(12):
    # atribuindo uma quantidade aleatória por mes de 0 a 4.
    vezes_que_posso_sair.append(randrange(0, 5)) 
    
x = meses_do_ano
y = vezes_que_posso_sair

# Configurações para plotar a tabela
plt.figure(figsize=(12, 4))

plt.plot(x, y, marker='o')
plt.title('Quantidade permitida para sair')
plt.yticks(range(0, 5))
plt.grid()
plt.show()