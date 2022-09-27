import numpy as np

count = np.arange(10)

data = np.array([[44410, 5712, 37123, 0, 25757],
                 [2003, 1991, 1990, 2019, 2006]])


"""    I am going to show some attributes of the numpy    """

# # shape: show in tuple the quantity of lines and columns of array
# print(data.shape)
#
# # ndim: show the number of dimensions of the array
# print("Quantity of the dimensions: ", data.ndim)
#
# # size: show the numbers of the element in an array
# print(data.size)  # Lines x Columns = Size
#
# # dtype: data type in array
# print(data.dtype)
#
# # T or transpose: show of the inverse form the line and column
# print("\n'.T'")
# print(data.T)
# print("\n'transpose'")
# print(data.transpose())


"""    I am going to show some methods of the numpy    """

# # tolist: Transform numpy array to numpy list
# print(data.tolist())
#
#
# #                       The Method reshape
# # like the name said give the new form to body of the array in this case
# # I am going to use the array count suppose that I want this array with
# # shape 2 lines and 5 columns ever have in your mind that the product of
# # this multiplication need be the same size of the array
# print(count.reshape((5, 2), order='F'))
#
# km_list = [44410, 5712, 37123, 0, 25757]
# year_list = [2003, 1991, 1990, 2019, 2006]
#
# # If I have this case I can use reshape to ordered my visualization
# # but, obviously I need transform these lists to arrays
# year_and_km_list = km_list + year_list
# print(year_and_km_list)
#
# # for example for each km I have respective year of fabrication:
# print(np.array(year_and_km_list).reshape((5, 2), order='F'))
#
# # resize: Make a new line into of the array
# data_new = data.copy()
# data_new.resize((3, 5))
# print(data_new)
#
# # To put average in the new line
# data_new[2] = data_new[0] / (2022 - data_new[1])
# print(data_new)


