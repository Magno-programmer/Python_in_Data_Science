import pandas as pd


"""             Using the query             """


pd.set_option('expand_frame_repr', False)

data_set = pd.read_csv('../data/db.csv', sep=';', index_col=0)

# when the name of column is simple for example 'Motor' I can call
# in this form
print(data_set.Motor, '\n')  # Return a Series With column motor

# If I want a parameter for example 'Motor diesel' inside motor
# I can do comparation, and will return boolean values
# for all rows
select_motor_type = data_set.Motor == 'Motor Diesel'
print(type(select_motor_type), '\n')  # return series

# If I put it in '[]' going to return to me only true values
# will show me all cars with motor diesel
print(data_set[select_motor_type], '\n')

# I can put another select too, for example I want a car diesel
# and zero km
print(data_set[(data_set.Motor == 'Motor Diesel') & (data_set.Zero_km == True)], '\n')


"""                  I can use a method query              """

# To use the method query exist some difference of the
# data set common, I do not use '&, |' but, use 'and, or'
print(data_set.query("Motor == 'Motor Diesel' and Zero_km == True"))









