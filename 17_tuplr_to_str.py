'''
Write a Python program to convert a tuple to a string.
'''
def tuple_to_string(input_tuple):
    tuple_string = ''.join(map(str, input_tuple))
    return tuple_string

my_tuple = (1, 2, 3, 4, 5)
tuple_string = tuple_to_string(my_tuple)

print("Original Tuple:", my_tuple)
print("Tuple as String:", tuple_string)
