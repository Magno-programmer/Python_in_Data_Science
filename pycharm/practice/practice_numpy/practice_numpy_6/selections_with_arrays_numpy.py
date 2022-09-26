# importing numpy library renaming as np
import numpy as np

"""   Making an array with 10 positions 
                (0 until 9)         """

count = np.arange(10)
print(count)


"""     for slice from I until J(exception) 
              you can use arr[i:j]      """

# # This going to print index 1, 2, 3 and going to stop in 4
# print(count[1:4])


"""     for slice from I until J(exception) jumping K numbers 
                    you can use arr[i:j:k]                  """

# # This going to print index 1, 3, 5, 7 and going to stop in 8
# print(count[1:8:2])
#
# # This going to print all index even
# print(count[::2])
#
# # This going to print all index odd
# print(count[1::2])
#


"""     Making an array with data where the value of the
            line 1(index 0) are km and the value of
            the line 2(index 1) are year fabrication      """

data = np.array([[44410, 5712, 37123, 0, 25757],
                 [2003, 1991, 1990, 2019, 2006]])
#
# # If I want to pick up just the index 1 and 2 of this array
# # from the two lines I do it
# print(data[:, 1:3])
#
# # I can do the average of the km with these arrays look below
# #                       line
# km_average = data[:, 1:3][0] / (2019 - data[:, 1:3][1])
# #                                                  line
# print(km_average)


"""     for print just the boolean value 
          we can to use the array too     """

print(count)
# This line going to print false for all index that is less than five
print(count > 5)

# count have just one dimension so if I put it like parameter
# it is going to print only 'true' values
print(count[count > 5])

# if I to use now the data I can do the average of the different form
print(data)

# If I want to pick up just the years greater than 2000
print(data[1] > 2000)

# To calculate average of the km of these years
# First I selected all km of the cars with years greater than 2000
selection = data[:, data[1] > 2000]

# and then I do a division pick up the values of km with cars have greater than two thousand
# with the subtraction of years from data and my current year
average_years = selection[0] / (2022 - selection[1])
print(average_years)







