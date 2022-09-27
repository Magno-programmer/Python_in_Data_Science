
name_list = ["Gol", "Chevrolet", "Fiat Uno", "Palio"]
km_list = [44410.0, 5712.0, 37123.0, 0.0, 25757.0]
names_car = ("Gol", "Chevrolet", "Fiat Uno", "Palio")

print(names_car)


"""          unpacking tuple values       """

# a tuple can be passed to another variables of a different form
car_1, car_2, car_3, car_4 = names_car
print(car_1, car_2, car_3, car_4)


# I can change a list to tuple with '.zip()'
creating_a_tuple = zip(name_list, km_list)
print(creating_a_tuple)

# To Print the values in, you can transform this zip to list
creating_a_tuple = list(creating_a_tuple)
print(creating_a_tuple, "\n")

# I can also print with a looping 'for' with a zip:
for item in zip(name_list, km_list):
    print(item, "\n")

# # I can also pass two values in 'for' to give me a print separated
# # to unpack the tuple
# for name_list, km_list in zip(name_list, km_list):
#     print(name_list, km_list)

# If I want to print just a type of values I can use a conditional 'if' in 'for'
for name_list, km_list in zip(name_list, km_list):
    if km_list > 20000:
        print(name_list)












