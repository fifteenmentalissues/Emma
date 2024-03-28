import numpy as np

num_string = input("Input list of numbers")
num_list = num_string.split()
for i in range(len(num_list)):
    num_list[i] = int(num_list[i])

for i in range(len(num_list)):
    num_list[i] = num_list.unique()

print(num_li
# incomplete