'''
Write a Python program to check a list is empty or not.
'''
def empty(input_list):
    return not input_list

list1 = [1,2]

if empty(list1):
    print("Yes")
else:
    print("No")
