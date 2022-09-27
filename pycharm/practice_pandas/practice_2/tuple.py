
# A tuple is like a list, but the difference that it is immutable,
# so I never can change the value of the tuple, and it is declared
# with parentheses not square brackets


""" I am going to show some forms to make a tuple in python """


# first form: just putting a parentheses
print(())

# second form: putting sequence of numbers separate with comma
numbers = 1, 2, 3
print(numbers)

# Third form: putting variables in parentheses separate with comma
name_car = "Gol"
price_car = 24000
print((name_car, price_car))

# fourth form: declaring a variable with a list in tuple
names_cars = tuple(["Gol", "Chevrolet", "Fiat Uno", "Palio"])
print(names_cars)

# If I want see the type of this variable If really is a tuple
print(type(names_cars))















