'''
Write a Python program to find the highest 3 values in a dictionary
'''
import heapq

def find_highest_values(dictionary, n=3):
    highest_values = heapq.nlargest(n, dictionary.values())
    return highest_values

example_dict = {'a': 100,'b': 200,'c': 300,'d': 400,'e': 500,'f': 50}

highest_3_values = find_highest_values(example_dict)

print("Highest 3 values:", highest_3_values)
