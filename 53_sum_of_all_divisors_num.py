'''
Write a Python program to returns sum of all divisors of a number
'''
def sum_of_divisors(n):
    if n <= 0:
        return 0
    sum_divisors = 0

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
    
    return sum_divisors

number = 28 
result = sum_of_divisors(number)
print(f"The sum of all divisors of {number} is: {result}")
