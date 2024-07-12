'''
Write a Python program to remove duplicates from a list.
'''
def remove_duplicates(input_list):
    return list(set(input_list))

l1 = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
l2 = remove_duplicates(l1)
print(l1)
print(l2)
