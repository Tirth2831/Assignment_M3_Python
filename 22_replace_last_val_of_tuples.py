'''
Write a Python program to replace last value of tuples in a list.
'''
def replace_last_value(tuples_list, new_value):
    updated_tuples = []
    for tup in tuples_list:
        list_version = list(tup)
        list_version[-1] = new_value
        updated_tuples.append(tuple(list_version))
    return updated_tuples

tuples_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_value = 100

updated_list = replace_last_value(tuples_list, new_value)
print("Original List of Tuples:", tuples_list)
print("Updated List of Tuples:", updated_list)
