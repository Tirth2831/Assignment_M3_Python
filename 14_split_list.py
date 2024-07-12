'''
Write a Python program to split a list into different variables.
'''
def split_list_into_variables(input_list):
    if len(input_list) < 3:
        return None  
    var1, var2, var3 = input_list[:3]
    
    return var1, var2, var3

my_list = [1, 2, 3, 4, 5]
result = split_list_into_variables(my_list)

if result is not None:
    var1, var2, var3 = result
    print("Variable 1:", var1)
    print("Variable 2:", var2)
    print("Variable 3:", var3)
else:
    print("List does not have enough elements to split.")
