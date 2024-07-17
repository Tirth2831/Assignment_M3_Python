'''
Write a Python program to check multiple keys exists in a dictionary
'''
def check_keys_exist(dictionary, keys):
    return all(key in dictionary for key in keys)

my_dict = {'a': 1, 'b': 2,'c': 3, 'd': 4}

keys_to_check = ['a', 'b', 'c']

result = check_keys_exist(my_dict, keys_to_check)
print(f"Do all keys {keys_to_check} exist in the dictionary? {result}")

keys_to_check = ['a', 'b', 'x']
result = check_keys_exist(my_dict, keys_to_check)
print(f"Do all keys {keys_to_check} exist in the dictionary? {result}")
