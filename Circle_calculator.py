# This program is going to compute
# the diameter, circumference,  surface area
# and volune of a sphere when the radius is
# given by the user.

# Formulas
# Diameter = 2 * r
# Circumference = diameter * pi
# Surface area = 4 * pi * radius squared
# Volume = 4/3 * pi * radius cubed

# Import Math
import math

# Main Function
def main():
    # Get the input
    radius = float(input("Enter the radius of the circle: "))
    # Compute the results
    diameter = 2 * radius
    curcumference = diameter * math.pi
    surfaceArea = 4* math.pi * radius * radius
    volume = 4/3 * math.pi * radius * radius * radius
    # Call show_calc function
    show_calc(radius,diameter,curcumference,surfaceArea,volume)

# Show_calc Function
def show_calc(radius,diameter,curcumference,surfaceArea,volume):
    # Display the results
    print('The given radius of the circles is', \
      format(radius,',.2f'))
    print('The diameter of the circles is', \
      format(diameter,',.2f'))
    print('The curcumference of the circles is', \
      format(curcumference,',.2f'))
    print('The surfaceArea of the circles is', \
      format(surfaceArea,',.2f'))
    print('The volume of the circles is', \
      format(volume,',.2f'))

# Call the main function
main()
                     
