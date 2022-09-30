import numpy as np
import pandas as pd

# pd.set_option('Display.max_rows', None)
# pd.set_option('Display.max_columns', None)
pd.set_option('expand_frame_repr', None)

cars = pd.read_csv('cars/cars.csv', sep=';', index_col=0)
df = pd.DataFrame(cars)
# print(df)
# print(df.info())
df['zero_km'] = df['zero_km'].astype(bool)  # change type to boolean
print(df)
# print(df.query('zero_km == True'), '\n')

# If I want the average of prices

print("This is the average price of all car: ")
print("R$%.2f" % df['preço'].mean(), '\n')

print("This is the patrimonial value of the cars: ")
print("R$%.2f" % sum(df['preço']))


