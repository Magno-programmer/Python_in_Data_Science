
dictionary = {'Gol': 44410.0, 'Chevrolet': 5712.0, 'Fiat Uno': 37123.0, 'palio': 22000.8, 'muscat': 150000}


"""    I will do Iterating about dictionary in python   """


# '.keys()' return a list with all keys from dictionary
print(dictionary.keys())

# '.values()' return a list with all values from dictionary
print(dictionary.values())

# '.items()' return a list with all keys and values from dictionary
# in tuple format
print(dictionary.items())

# I can do the same thing of did in tuple, to unpack with looping for
print('\n')
for key, value in dictionary.items():
    print(key)
print('\n')
# or
for key, value in dictionary.items():
    print(value)
print('\n')
# or with a conditional
for key, value in dictionary.items():
    if value > 20000:
        print(key)
















