'''
Write a Python program to remove an empty tuple(s) from a list of tuples.
'''
def remove_empty_tuples(list_of_tuples):
    filtered_list = [tup for tup in list_of_tuples if tup]
    return filtered_list

list_of_tuples = [(1, 2), (), (3, 4, 5), (), (), (6), ()]

filtered_list = remove_empty_tuples(list_of_tuples)
print("Original List of Tuples:", list_of_tuples)
print("List of Tuples without Empty Tuples:", filtered_list)
