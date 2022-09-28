
dictionary = {"Gol": 44410.0, "Chevrolet": 5712.0, "Fiat Uno": 37123.0}


"""   Using some methods to dictionary   """


# '.update()' I can put new information, and update of existed information
dictionary.update({'palio': 22000.8, 'muscat': 150000})
print(dictionary)

# I can copy data and modify copy without to modify origin
dictionary_copy = dictionary.copy()
del dictionary_copy['Gol']
print("\n", dictionary)
print(dictionary_copy, "\n")

# '.pop()' remove a key and show the value of the element removed
print(dictionary_copy.pop('palio'))

# there is a parameter from '.pop()' that not leave happen an error
# if the key not exist
print(dictionary_copy.pop('palio', 'this car not exist'))

# '.clear()' clear all dictionary
dictionary_copy.clear()
print(dictionary_copy)


















