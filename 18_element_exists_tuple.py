'''
Write a Python program to check whether an element exists within a
tuple.
'''
def element_exists_in_tuple(input_tuple, element):
    return element in input_tuple

my_tuple = (1, 2, 3, 4, 5)

element_to_check1 = 3
element_to_check2 = 6

print("Tuple:", my_tuple)
print(f"Element {element_to_check1} exists:", element_exists_in_tuple(my_tuple, element_to_check1))
print(f"Element {element_to_check2} exists:", element_exists_in_tuple(my_tuple, element_to_check2))
