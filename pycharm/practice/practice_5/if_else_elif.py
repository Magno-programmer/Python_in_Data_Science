# list
data = [
    ['Jetta Variant', 2003, False],
    ['Passat', 1991, False],
    ['Crossfox', 1990, False],
    ['DS5', 2019, True],
    ['Aston Martin DB4', 2006, False],
    ['Palio Weekend', 2012, False],
    ['A5', 2019, True],
    ['Série 3 Cabrio', 2009, False],
    ['Dodge Jorney', 2019, False],
    ['Carens', 2011, False]
]

"""  looping with if, else, elif and conditional(and, or, not)  """

# # Making a 'for' with 'if-else' to check cars 0 km
# car_km0, car_used = [], []
#
# for item in data:
#     if item[2] is False:
#         car_used.append(item)
#     else:
#         car_km0.append(item)
#
# print("This car is used: ", list(car_used))
# print("\nThis car is 0 km: ", list(car_km0))

""" In python is possible do comparation with a variable
    and two values with its, one in left and one in right, look it"""

car_new, car_semi_new, car_old = [], [], []

for item in data:
    if item[1] < 2010:
        car_old.append(item)
    elif 2010 < item[1] < 2015:  # this there is just in python!
        car_semi_new.append(item)
    else:
        car_new.append(item)

print("These are old cars: ", car_old)
print("\nThese are semi new cars: ", car_semi_new)
print("\nThese are new cars: ", car_new)

