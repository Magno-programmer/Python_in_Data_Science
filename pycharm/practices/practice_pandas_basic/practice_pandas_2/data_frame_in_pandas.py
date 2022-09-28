import pandas as pd


"""     I will start learn about DataFrame in library pandas     """


data_list = [
    {'Nome': 'Jetta Variant', 'Motor': 'Motor 4.0 Turbo', 'Ano': 2003,
     'Quilometragem': 44410.0, 'Zero_km': False, 'Valor': 88078.64},

    {'Nome': 'Passat', 'Motor': 'Motor Diesel', 'Ano': 1991,
     'Quilometragem': 5712.0, 'Zero_km': False, 'Valor': 106161.94},

    {'Nome': 'Crossfox', 'Motor': 'Motor Diesel V8', 'Ano': 1990,
     'Quilometragem': 37123.0, 'Zero_km': False, 'Valor': 72832.16}
]

data_dictionary = {
    'Nome': ['Jetta Variant', 'Passat', 'Crossfox'],
    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8'],
    'Ano': [2003, 1991, 1990],
    'Quilometragem': [44410.0, 5712.0, 37123.0],
    'Zero_km': [False, False, False],
    'Valor': [88078.64, 106161.94, 72832.16]
}


"""     Some forms to use the Data Frame to extract 
            a information in format of table            """

#
# # for I to post the list 'data' in form of the table, I can use '.DataFrame()'
# # the DataFrame need be to each first case as uppercase
# data_set_list = pd.DataFrame(data_list)
# print(data_set_list, '\n')
#
# # If I want to change the order of the column I can use double square brackets
# # when call variable
# print(data_set_list[['Nome', 'Ano', 'Motor', 'Quilometragem', 'Zero_km', 'Valor']], '\n')
#
# # And this form is the same thing to make a DataFrame through dictionary
# data_set_dic = pd.DataFrame(data_dictionary)
# print(data_set_dic)


"""                Data Frame to external files                 """


# # If you want delimiter numbers of columns and rows you can use the
# # set_option, and define the max rows and columns, also decide if
# # your table will show complete in screem
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
pd.set_option('expand_frame_repr', False)
"""the default of the max rows and columns is 10"""

# I can pick up excel table and show here with 'read_csv', for no give an error
# you need pass a 'sep' that is the thing that you used to separate columns'
# data_set_table = pd.read_csv('../data/db.csv', sep=';')
# print(data_set_table)

# I can change the first columns on my table, with 'index_col = <value of index>'
data_set_table = pd.read_csv('../data/db.csv', sep=';', index_col=0)
print(data_set_table)






