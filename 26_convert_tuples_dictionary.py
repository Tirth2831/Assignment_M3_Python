'''
Write a Python program to convert a list of tuples into a dictionary.
'''
def list_of_tuples_to_dict(list_of_tuples):
    dictionary = {key: value for key, value in list_of_tuples}
    return dictionary

list_of_tuples = [("a", 1), ("b", 2), ("c", 3)]

converted_dict = list_of_tuples_to_dict(list_of_tuples)
print("List of Tuples:", list_of_tuples)
print("Converted Dictionary:", converted_dict)
