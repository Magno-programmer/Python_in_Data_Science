import numpy as np

names_cars = np.loadtxt('cars/cars-names.txt', dtype=str)
price_cars = np.loadtxt('cars/cars-prices.txt', dtype=float)
years_cars = np.loadtxt('cars/cars-years.txt', dtype=int)
km_cars = np.loadtxt('cars/cars-km.txt', dtype=float)
zero_km_cars = np.loadtxt('cars/cars-zero-km.txt', dtype=int)

info_cars = (names_cars.tolist() + price_cars.tolist() + years_cars.tolist() + km_cars.tolist())
info_graph = np.array(info_cars).reshape((258, 4), order='F')

print(info_graph)









