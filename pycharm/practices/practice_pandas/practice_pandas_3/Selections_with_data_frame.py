import pandas as pd

"""remove comment only to see complete table"""
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
pd.set_option('expand_frame_repr', False)

data_set = pd.read_csv('../data/db.csv', sep=';', index_col=0)
# with data_set.head() show the first 5 lines from csv
print(data_set.head(), "\n")

# # I can to select just one column from cvs and how I passed
# # the index like name(column index 0) the 'index' that
# # stay with the value showed was the name of cars
# print(data_set['Valor'])
#
# # let see the type of it, the data frame is a type of series group
# # it is going to show the type series if I select only one
# print(type(data_set['Valor']), "\n")
#
# # If I want that type of it be data frame I need put two square brackets
# print(data_set[['Valor']])
# print(type(data_set[['Valor']]))


"""               How do work the '.loc()' and '.iloc()'             """


# # If I want return all info about one row I can to use .loc[]
# # with one square bracket and two square bracket return
# # information in data frame, and is necessary for more that
# # one row selected
# print(data_set.loc['Passat'], "\n")  # Series
# print(data_set.loc[['Passat']], "\n")  # Data Frame
#
# # to select a line I use one square bracket and to select
# # a column I separate with comma and use two square bracket
# print(data_set.loc[['Passat', 'DS5'], ['Motor', 'Valor']], '\n')
#
# # and if I want delimiter just rows I can use just colon
# print(data_set.loc[:, ['Motor', 'Valor']], '\n')


"""               How do work the '.iloc()'             """


# different of the .loc that select through names, this select type pick up through the index
print(data_set.iloc[0], "\n")  # return in Series the first row
print(data_set.iloc[[0]], "\n")  # return in Data Frame the first row

# I can use the slice in this case too
# return in Data Frame the first, second and stop in third row
print(data_set.iloc[1:3], "\n")

# if I want a specific column I can use comma and other square bracket,
# indicating with index too in the same order that I to put
# return in Data Frame the first, second and stop in third row show three columns
print(data_set.iloc[1:3, [0, 5, 2]], "\n")

# and if I want delimiter just rows I can use just colon
print(data_set.iloc[:, [0, 5, 2]], '\n')

# I can also select specific rows
print(data_set.iloc[[0, 250, 22], [0, 2, 5]], '\n')












