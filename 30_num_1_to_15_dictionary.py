'''
Write a Python script to print a dictionary where the keys are numbers
between 1 and 15.
'''
num_dict = {}

for i in range(1, 16):
    num_dict[i] = i ** 2

print(num_dict)
