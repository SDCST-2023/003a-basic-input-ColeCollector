#! python3
# Find the volume of a sphere.
# You will ask the user to enter the radius of the sphere.
# Calculate the Volume and then display the result to the user.
# You will need to import the math module in order to use math.pi

# Inputs:
# radius
#
# Outputs
# volume
#
# test output radius of 3 should give volume of 113.09733552923254

radius = input("Please enter the radius you would like for your sphere. ")
radius = float(radius)
volume = (4/3)*3.14159265359*radius**3
print("The volume of your sphere is", volume)