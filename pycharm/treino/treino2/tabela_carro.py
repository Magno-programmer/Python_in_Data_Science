import numpy as np

# usando a biblioteca numpy para pegar arquivo txt
km = np.loadtxt("./carros/carros-km.txt")
anos = np.loadtxt("./carros/carros-anos.txt")

# Tirando média com os arquivos usados
km_media = km / (2022 - anos)

# Olhando a média
print(' '*10, '-'*10, 'Média dos carros', '-'*10)
print(km_media)
