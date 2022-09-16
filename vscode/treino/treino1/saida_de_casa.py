from random import randrange
import matplotlib.pyplot as plt

meses_do_ano = ['Janeiro', 'Fevereiro', 'Março',
                'Abril', 'Maio', 'Junho', 
                'Julho', 'Agosto', 'Setembro', 
                'Outubro', 'Novembro', 'Dezembro']

vezes_que_posso_sair = []

for x in range(12):
    vezes_que_posso_sair.append(randrange(0, 5))
    
x = meses_do_ano
y = vezes_que_posso_sair

plt.figure(figsize=(12, 4))

plt.plot(x, y, marker='o')
plt.title('Quantidade permitida para sair')
plt.yticks(range(0, 5))
plt.grid()
plt.show()