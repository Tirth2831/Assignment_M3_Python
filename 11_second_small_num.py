'''
Write a Python program to find the second smallest number in a list.
'''
def second_smallest(numbers):
    if len(numbers) < 2:
        return None
    
    smallest = float('inf')
    second_smallest = float('inf')
    
    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    
    return second_smallest

my_list = [5, 2, 7, 3, 8, 1]
result = second_smallest(my_list)

if result is not None:
    print("Second smallest number:", result)
else:
    print("List is too short to find the second smallest number.")
