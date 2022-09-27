# Importing the library numpy and time
import numpy as np
import time

"""     making arrays from list and 
          looking the data type           """

# testing_array = np.array([10, 20, 30, 40])
# print(testing_array)
#
# #  the data type
# # the data type of the array
# print(type(testing_array))
#
# # the data type of the values of array
# print(testing_array.dtype)


"""     making array from external data and 
          looking the dimension of array         """

# cars_km = np.loadtxt(fname='../../cars/cars-km.txt', dtype=int)
# print(cars_km)
#
# data_cars = [
#     ['Jetta Variant', 2003, False],
#     ['Passat', 1991, False],
#     ['Crossfox', 1990, False],
#     ['DS5', 2019, True],
#     ['Aston Martin DB4', 2006, False],
#     ['Palio Weekend', 2012, False],
#     ['A5', 2019, True],
#     ['Série 3 Cabrio', 2009, False],
#     ['Dodge Jorney', 2019, False],
#     ['Carens', 2011, False]
# ]
#
# # Difference of the shapes'
# cars = np.array(data_cars)
# data_cars_dimension = cars.shape
# km_dimension = cars_km.shape
# print("the shape of list km: ", km_dimension)
# print("the shape of list of data cars: ", data_cars_dimension)


""""       show the difference of performance 
                with the 'time' method              """


# def function():
#     nump_array = np.arange(1000000)
#     for x in range(100):
#         nump_array *= 2
#
#
# start_1 = time.time()
# function()
# end_1 = time.time()
#
# print("The functon one do it in: seconds", end_1 - start_1)
#
#
# def function2():
#     python_list = list(np.arange(1000000))
#     for x in range(100):
#         python_list = [x * 2 for x in python_list]
#
#
# start_2 = time.time()
# function2()
# end_2 = time.time()
#
# print("the function two do it in: seconds", end_2 - start_2)
