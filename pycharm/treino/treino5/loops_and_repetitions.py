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


