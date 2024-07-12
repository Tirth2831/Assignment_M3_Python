'''
Write a Python function to get the largest number, smallest num and sum
of all from a list.
'''
def get_num(numbers):
    if not numbers:
        return None, None, 0
    
    largest = max(numbers)
    smallest = min(numbers)
    total_sum = sum(numbers)
    
    return largest, smallest, total_sum

l = [2, 33, 222, 14, 25]
largest_num, smallest_num, sum_all = get_num(l)

print("List:", l)
print("Largest number:", largest_num)
print("Smallest number:", smallest_num)
print("Sum of all numbers:", sum_all)
