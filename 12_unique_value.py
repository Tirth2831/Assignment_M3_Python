'''
Write a Python program to get unique values from a list
'''
def get_unique_values(input_list):

    unique_values_set = set(input_list)
    unique_list_set = list(unique_values_set)
    
    unique_list_dict = list(dict.fromkeys(input_list))
    
    return unique_list_set, unique_list_dict

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set, unique_dict = get_unique_values(my_list)

print("Original List:", my_list)
print("Unique Values (Set Method):", unique_set)
print("Unique Values (Dictionary Method):", unique_dict)
