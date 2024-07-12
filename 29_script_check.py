'''
Write a Python script to check if a given key already exists in a
dictionary'''

def check_key_in_dict(input_dict, key):
    return key in input_dict

my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_check1 = 'b'
key_to_check2 = 'd'

print("Dictionary:", my_dict)
print(f"Key '{key_to_check1}' exists:", check_key_in_dict(my_dict, key_to_check1))
print(f"Key '{key_to_check2}' exists:", check_key_in_dict(my_dict, key_to_check2))
