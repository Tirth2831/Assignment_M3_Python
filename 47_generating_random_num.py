'''
How will you set the starting value in generating random numbers?
'''
import random

random.seed(42)

print(random.randint(1, 100))   
print(random.random())   
print(random.uniform(10.5, 20.5)) 
print(random.choice(['apple', 'banana', 'cherry']))
