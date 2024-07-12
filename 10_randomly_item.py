'''
Write a Python program to select an item randomly from a list.
'''
import random

def select_random_item(items):
    if not items:
        return None
    return random.choice(items)

my_list = ["apple", "banana", "cherry", "date", "elderberry"]
random_item = select_random_item(my_list)
print("Randomly selected item:", random_item)
