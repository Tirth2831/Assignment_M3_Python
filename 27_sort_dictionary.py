'''
Write a Python script to sort (ascending and descending) a dictionary by
value
'''
import operator

def sort_dict_by_value_ascending(input_dict):
    sorted_dict = dict(sorted(input_dict.items(), key=operator.itemgetter(1)))
    return sorted_dict

my_dict = {'a': 5, 'b': 2, 'c': 7, 'd': 1}

sorted_dict_asc = sort_dict_by_value_ascending(my_dict)
print("Original Dictionary:", my_dict)
print("Dictionary sorted by value (ascending):", sorted_dict_asc)

def sort_dict_by_value_descending(input_dict):
    sorted_dict = dict(sorted(input_dict.items(), key=operator.itemgetter(1), reverse=True))
    return sorted_dict

sorted_dict_desc = sort_dict_by_value_descending(my_dict)
print("Dictionary sorted by value (descending):", sorted_dict_desc)
