'''
Write a Python function to check whether a number is in a given range
'''
def in_range(num, start, end):
    return start <= num <= end
print(in_range(5, 1, 10))
print(in_range(15, 1, 10)) 
print(in_range(-1, -10, 0))
