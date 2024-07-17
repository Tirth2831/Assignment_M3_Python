'''
Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary.
Sample data: {'1': ['a','b'], '2': ['c','d']}
Expected Output:
ac ad bc bd
'''
import itertools

def display_combinations(data):

    values = data.values()
    combinations = itertools.product(*values)
    
    for combination in combinations:
        print(''.join(combination))

data = {'1': ['a', 'b'], '2': ['c', 'd']}

display_combinations(data)
