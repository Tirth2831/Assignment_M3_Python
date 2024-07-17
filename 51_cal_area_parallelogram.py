'''
Write a Python program to calculate the area of a parallelogram
'''
def parallelogram_area(base, height):
    area = base * height
    return area

base_length = 5  
height_length = 7

area = parallelogram_area(base_length, height_length)
print(f"The area of the parallelogram with base {base_length} and height {height_length} is: {area}")
