import numpy as np

price_cars = np.loadtxt('../../cars/cars-prices.txt', dtype=float)
years_cars = np.loadtxt('../../cars/cars-years.txt', dtype=int)
km_cars = np.loadtxt('../../cars/cars-km.txt', dtype=float)


""" More some methods in numpy """

# # columns_stack: for When I want to organize files in columns
table = np.column_stack((years_cars, price_cars, km_cars))
print(table.shape)

# mean: you can do average of the code
print(np.mean(table))
# if we leave this form, stay stranger because will make an average
# about all data and all columns, so for resolve it, I use 'axis'
# delimiter the column, and make a average with each column
print(np.mean(table, axis=0))

# I can use the 'mean' with slice too for select one column specific
print(np.mean(table[:, 1]))

# std: is the same thing that mean, but, will calculate the standard deviation
print(np.std(table[:, 1]))

# sum: make a sum of the column of the table there is many forms to do it
# this return a line with all columns summing
print(table.sum(axis=0))

# this return the column selected summed
print(table[:, 1].sum())

# return the same thing that 'table.sum()'
print(np.sum(table, axis=0))

# making slice in all element of the column this method sum they
print(np.sum(table[:, 1]))
