'''
Write a Python program to map two lists into a dictionary
'''
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]

mapped_dict = dict(zip(keys, values))

print("Mapped Dictionary:", mapped_dict)
