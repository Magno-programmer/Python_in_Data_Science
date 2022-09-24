""" Introduction 'for' """

# in the first moment I will make a list null of squares
square = []

# every time I want from a number through other I can to use 'range' function
# for each element that I want to put in list I 'append' in it using 'append' attribute
# in a for looping
for x in range(10):  # x going to start with 0 and through to each number until 9
    square.append(x ** 2)  # for each element 'x' I appended the square their in list

print(square)

# I get make the same thing with 2 code-line
square_in_one_line = [x ** 2 for x in range(10)]
print(square_in_one_line)


""" ******* removing duplicates ******** """

# to make it, I can use the method 'set'
names_of_subscription = ["carlos", "luciana", "gustavo", "alice", "joao",
                         "andre", "augusto", "jorge", "heloisa", "camila",
                         "george", "anderson", "benir", "benjamin", "paula",
                         "leo", "lucas", "Jersica", "aparecida", "maria"]

names_permitted = ["joao", "Alexandro", "Joasir", "John", "carlos", "luciana",
                   "alencar", "aparecida", "mateus", "thiago", "bernardo", "leo"]

# if I concatenate lists going to show all elements inclusive duplicate
every_names_with_duplicate = names_of_subscription + names_permitted
print(every_names_with_duplicate)
print("\nall element counted in list with duplicate: ", len(every_names_with_duplicate), "\n\n")

# but if I put this list in method 'set', going to be removed every duplicate name
every_names_without_duplicate = list(set(names_of_subscription + names_permitted))
print(every_names_without_duplicate)
print("\nall element counted in list without duplicate: ", len(every_names_without_duplicate))

""" ******* 'for' inside of 'for' ******** """

names = [["carlos", "luciana", "gustavo", "alice", "joao",
         "andre", "augusto", "jorge", "heloisa", "camila",
         "george", "anderson", "benir", "benjamin", "paula",
         "leo", "lucas", "Jersica", "aparecida", "maria"],
         ["joao", "Alexandro", "Joasir", "John", "carlos",
          "luciana", "alencar", "aparecida", "mateus", "thiago",
          "bernardo", "leo"]]

# This is a normal looping 'for', where there is just one command
# This 'for' going to print the two list on separated form
for _list in names:
    print(_list)

# In this case, there are two for, one inside other that will print
# the list complete
for _list in names:
    for all_names_common in _list:
        print(all_names_common)

# When I make a list to put the two list together I am creating a new list
all_names_list = []

for _list in names:
    for all_names_common in _list:
        all_names_list.append(all_names_common)

print(all_names_list)


# # this case I can to use also the set to remove duplicate
accessed = set(all_names_list)
print(accessed)

# # If I to want change it to list I can put function 'list'
list_of_accessed = list(set(all_names_list))
print(list_of_accessed)

# now you can to know if there is less element than another list
print(all_names_list)
print("The length of the list with duplicate is: ", len(all_names_list))
print("\n", list_of_accessed)
print("The length of the list without duplicate is: ", len(list_of_accessed))

