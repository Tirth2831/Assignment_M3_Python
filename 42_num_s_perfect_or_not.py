'''
Write a Python function to check whether a number is perfect or not.
'''
def is_perfect_number(num):
    if num <= 0:
        return False
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num

print(is_perfect_number(6))   
