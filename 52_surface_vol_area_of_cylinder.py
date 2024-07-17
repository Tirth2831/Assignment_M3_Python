'''
Write a Python program to calculate surface volume and area of a
cylinder'''

import math

def cylinder_surface_area_and_volume(radius, height):
   
    lateral_area = 2 * math.pi * radius * height
    base_area = 2 * math.pi * radius**2
    total_area = lateral_area + base_area
    
    volume = math.pi * radius**2 * height
    
    return total_area, volume

radius = 3.5  
height = 10 

surface_area, volume = cylinder_surface_area_and_volume(radius, height)
print(f"The surface area of the cylinder is: {surface_area:.2f} square units")
print(f"The volume of the cylinder is: {volume:.2f} cubic units")
