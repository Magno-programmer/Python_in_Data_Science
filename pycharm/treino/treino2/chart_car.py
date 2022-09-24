# importing numpy library
import numpy as np

# using numpy library to take .txt file
km = np.loadtxt("./carros/carros-km.txt")
years = np.loadtxt("./carros/carros-anos.txt")

# average of files in a variable
km_average = km / (2022 - years)

print(' '*10, '-'*10, 'Average of the cars', '-'*10)
print(km_average)
