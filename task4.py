#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912

import math
height = input("Please enter a height for your cone: ")
height = float(height)
radius = input("Please enter a radius for your cone: ")
radius = float(radius)
slant = math.sqrt((height**2) + (radius**2))
sa = 3.14159265359*(radius)*slant + 3.14159265359*(radius**2)
print("The surface area of your cone is", sa)
