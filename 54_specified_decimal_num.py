'''
Write a Python program to find the maximum and minimum numbers
from the specified decimal numbers
'''
def find_max_min(numbers):
    if not numbers:
        return None, None
    
    max_num = max(numbers)
    min_num = min(numbers)
    
    return max_num, min_num

decimal_numbers = [3.5, 1.2, 7.8, 4.1, 2.9]
max_number, min_number = find_max_min(decimal_numbers)

print(f"The maximum number is: {max_number}")
print(f"The minimum number is: {min_number}")
