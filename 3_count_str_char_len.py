'''
Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings.
'''
def count_strings(strings):
    count = 0
    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

strings_list = ['abc', 'xyz', 'aba', '1221', 'abaa']
result = count_strings(strings_list)
print(result)
