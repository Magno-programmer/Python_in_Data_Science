import numpy as np

names_cars = np.loadtxt('cars/cars-names.txt', dtype=str)
price_cars = np.loadtxt('cars/cars-prices.txt', dtype=float)
years_cars = np.loadtxt('cars/cars-years.txt', dtype=int)
km_cars = np.loadtxt('cars/cars-km.txt', dtype=float)
zero_km_cars = np.loadtxt('cars/cars-zero-km.txt', dtype=int)

info_graph = np.column_stack((names_cars, price_cars, years_cars, km_cars, zero_km_cars))
print(info_graph)









