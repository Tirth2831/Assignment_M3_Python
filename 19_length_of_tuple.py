'''
Write a Python program to find the length of a tuple.
'''
def tuple_length(input_tuple):
    return len(input_tuple)

my_tuple = (1, 2, 3, 4, 5)

length_of_tuple = tuple_length(my_tuple)
print("Tuple:", my_tuple)
print("Length of Tuple:", length_of_tuple)
