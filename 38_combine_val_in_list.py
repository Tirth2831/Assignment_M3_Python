'''
Write a Python program to combine values in python list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
300}, o {'item': 'item1', 'amount': 750}]
Expected Output:
Counter ({'item1': 1150, 'item2': 300})
'''
from collections import Counter

def combine_amounts(data):
    combined_counter = Counter()

    for entry in data:
        combined_counter[entry['item']] += entry['amount']
    return combined_counter

data = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]

combined_amounts = combine_amounts(data)

print("Combined amounts:", combined_amounts)
