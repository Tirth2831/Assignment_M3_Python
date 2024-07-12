'''
Write a Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30.
'''
def square():
    squares = [x ** 2 for x in range(1, 31)]
    return squares[:5] + squares[-5:]

result = square()
print(result)
