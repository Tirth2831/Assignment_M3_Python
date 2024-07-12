'''Write a Python program to convert a list to a tuple.'''

def list_to_tuple(input_list):
    tuple_from_list = tuple(input_list)
    return tuple_from_list

my_list = [1, 2, 3, 4, 5]

converted_tuple = list_to_tuple(my_list)
print("Original List:", my_list)
print("Converted Tuple:", converted_tuple)
