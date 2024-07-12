'''
Write a Python program to convert a list of characters into a string.
'''
def list_to_string(char_list):
    return ''.join(char_list)

char_list = ['H', 'e', 'l', 'l', 'o', ' ', 'T', 'o', 'p', 's']
result_string = list_to_string(char_list)

print(char_list)
print(result_string)
