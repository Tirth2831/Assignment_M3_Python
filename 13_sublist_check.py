'''
Write a Python program to check whether a list contains a sub list
'''
def is_sublist(main_list, sub_list):
    if len(sub_list) == 0:
        return True  
    if len(sub_list) > len(main_list):
        return False  
    for i in range(len(main_list) - len(sub_list) + 1):
        if main_list[i:i+len(sub_list)] == sub_list:
            return True
    
    return False

main_list = [1, 2, 3, 4, 5, 6, 7]
sub_list1 = [3, 4, 5]

print("Main List:", main_list)
print("Sub List 1:", sub_list1)
print("Sub List 1 is sublist:", is_sublist(main_list, sub_list1))
