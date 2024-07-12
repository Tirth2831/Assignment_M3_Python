'''
Write a Python program to find the repeated items of a tuple.
'''
from collections import Counter

def find_repeated_items(input_tuple):
    count_dict = Counter(input_tuple)
    
    repeated_items = [item for item, count in count_dict.items() if count > 1]
    
    return repeated_items

my_tuple = (1, 2, 3, 2, 4, 5, 3, 6, 3)
repeated_items = find_repeated_items(my_tuple)

print("Tuple:", my_tuple)
print("Repeated Items:", repeated_items)
