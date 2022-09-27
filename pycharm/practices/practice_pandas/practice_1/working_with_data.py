import pandas as pd

"""  ---   Settings to columns and rows show in correct form  ---  """

# # putting unlimited columns max
# pd.set_option('display.max_columns', None)
# # putting unlimited rows max
# pd.set_option('display.max_rows', None)
# # leave show all columns side by side
pd.set_option('expand_frame_repr', False)

# If I not select the display of pd, the default is 10 lines and columns

# I can pick up the csv file with pandas
dataset = pd.read_csv('../data/db.csv', sep=';')
print(dataset)

# I can see the data type of to each information in this table
print(dataset.dtypes)

# If I want select specifics information to know all
# the things about it, I can use 'describe'
# how I will select two information I need to use double square brackets
print(dataset[['Quilometragem', 'Valor']].describe())

# to know about all information of the table, you can use '.info()' attribute
print(dataset.info())



