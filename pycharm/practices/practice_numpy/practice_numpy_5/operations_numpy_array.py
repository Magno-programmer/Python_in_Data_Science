# importing numpy library renaming as np
import numpy as np

"""   with a list is not possible make a count 
            using a direct variable       """

# km_list = [44410, 5712, 37123, 0, 25757]
# year_list = [2003, 1991, 1990, 2019, 2006]
#
# # error
# years_old_list = year - 2019
# print(years_old)

"""    if I want to do an operation I can use numpy library
           and do a operation without convert nothing         """

km_array = np.array([44410, 5712, 37123, 0, 25757])
years_array = np.array([2003, 1991, 1990, 2019, 2006])

years_old_array = 2019 - years_array
print(years_old_array)

"""     better than seem, you can do operations
                with two arrays numpy           """

km_average = km_array / years_old_array
# When I to print it, it will give me an error because not exist division to 0
print(km_average)


