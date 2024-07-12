'''
Write a Python program to reverse a tuple.
'''
def reverse_tuple(input_tuple):
    reversed_tuple = tuple(reversed(input_tuple))
    return reversed_tuple

my_tuple = (1, 2, 3, 4, 5)

reversed_tuple = reverse_tuple(my_tuple)
print("Original Tuple:", my_tuple)
print("Reversed Tuple:", reversed_tuple)
