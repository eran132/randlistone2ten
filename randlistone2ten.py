# random module and specifically the shuffle method allows us to change the order of numbers in the range specified
import random

# Setting a variable equal to a list of numbers in the range of 1 to 10
num_list = list(range(11))

# Shuffling the order of numbers in the list inside the variable
random.shuffle(num_list)

# Finally, printing the the list to terminal
print(num_list)
