import numpy as np
import pandas as pd

pd.set_option('Display.max_rows', None)
pd.set_option('Display.max_columns', None)
pd.set_option('expand_frame_repr', None)

cars = pd.read_csv('cars/cars.csv', sep=';', index_col=0)
df = pd.DataFrame(cars)
# print(df)
# print(df.info())
df['zero_km'] = df['zero_km'].astype(bool)
# print(df)
print(df.query('zero_km == True & preço <= 70000'), '\n')


