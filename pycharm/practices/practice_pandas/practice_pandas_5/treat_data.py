import pandas as pd

pd.set_option('expand_frame_repr', False)
data_set = pd.read_csv('../data/db.csv', sep=';')


"""             treating datas               """

print(data_set.head(), '\n')

# To check information about my table I use '.info()'
print(data_set.info(), '\n')


"""     I can change the NaN value to 0 or remove all rows with it
                First changing to NaN value to 0             """


# # I saw that 'Quilometragem' are with some values NaN
# # To do it I need select all values NaN
# print(data_set[data_set.Quilometragem.isna()], '\n')
#
# # and then change these 'na' values to zero using
# # '.fillna()' putting the value 0, if I want to change in table truly
# # I need put more one parameter in fillna that is 'inplace = True'
# data_set.fillna(0, inplace=True)
# print(data_set, '\n')
#
# # If I want see if all vehicle zero_km are with rewrite na value to 0
# # I can check using the method query
# # Now If I do some model, these cars not will be removed.
# print(data_set.query("Zero_km == True"))


"""                  Removing all values NaN                   """

# I saw that 'Quilometragem' are with some values NaN
# To do it I need select all values NaN
print(data_set[data_set.Quilometragem.isna()], '\n')

# If these NaN is a problem to my table I can remove and,
# To remove all NaN I can use the '.dropna()' and
# in the parameter subset I put the column with NaN values, if I want to change in table truly
# I need put more one parameter in dropna that is 'inplace = True'
data_set.dropna(subset=['Quilometragem'], inplace=True)
print(data_set)







