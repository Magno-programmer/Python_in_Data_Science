
dictionary = {"Gol": 44410.0, "Chevrolet": 5712.0, "Fiat Uno": 37123.0}

"""      operations types about dictionary in python     """

# To access a value from in the dictionary you can use the key
print(dictionary["Gol"], "\n")

# This verifies if there is one key in dictionary and return True or False
print('Gol' in dictionary)
print('corn' in dictionary)
print('Chevrolet' in dictionary)

# the 'len()' to dictionary return the quantity of the keys
print("\n", len(dictionary))

# If I want to add some key on dictionary just use a square bracket to say
# a name key and to assign a value
dictionary['palio'] = 22000.90
print("\n", dictionary)

# And If I want to delete a key just to use 'del' before the dictionary with a key
del dictionary['palio']
print('\n', dictionary)















