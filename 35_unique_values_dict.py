'''
Write a Python program to print all unique values in a dictionary.
'''
def print_unique_values(dictionary):
    unique_values = set(dictionary.values())
    
    print("Unique values:", unique_values)

example_dict = {'a': 100,'b': 200,'c': 300,'d': 100,'e': 200,'f': 400}

print_unique_values(example_dict)
