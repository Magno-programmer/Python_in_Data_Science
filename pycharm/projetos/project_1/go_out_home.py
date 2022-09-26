# practicing python to Data Science
from random import randrange  # importing library random
import matplotlib.pyplot as plt  # importing library matplotlib

months_of_year = ["January", "February", "March",
                  "April", "May", "June",
                  "July", "August", "September",
                  "October", "November", "December"]

# list to receive the times I can go out in one month
times_I_can_go_out = []

# Looping to the twelve months
for x in range(12):
    # append random times from 0 through 4.
    times_I_can_go_out.append(randrange(0, 5))
    
x = months_of_year
y = times_I_can_go_out

# settings to chart
plt.figure(figsize=(12, 4))

plt.plot(x, y, marker='o')
plt.title('Times that I can to go out of home')
plt.yticks(range(0, 5))
plt.grid()
plt.show()
