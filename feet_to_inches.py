# The feet_to_inches function converter to inches.

# Constant for number of inches per foot
INCHES_PER_FOOT = 12 

# Main function
def main():
    # Get the number of foot from the user
    feet = int(input('Enter a number of feet? '))
    # Convert that to inches
    print(feet,'feet equals', feet_to_inches(feet), 'inches')
    
# The feet to inches converter
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

# Call to the function
main()
