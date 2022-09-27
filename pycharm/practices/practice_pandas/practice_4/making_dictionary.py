
name_list = ["Gol", "Chevrolet", "Fiat Uno", "Palio"]
km_list = [44410.0, 5712.0, 37123.0, 25757.0]

"""   The dictionaries are collections of between values even
        the first element of this even is Key, and second is Value  """


# I make a dictionary putting elements inside keys
# The dictionaries not be ordered because I have the access through keys, not index
dictionary = {"Gol": 44410.0, "Chevrolet": 5712.0, "Fiat Uno": 37123.0, "Palio": 25757.0}
print(dictionary)

# To confer the type of this variable
print(type(dictionary))

# I can make a dictionary also with the zip, using the build function 'dict()'
# and putting the zip inside it
dictionary_2 = dict(zip(name_list, km_list))
print(dictionary_2)


















