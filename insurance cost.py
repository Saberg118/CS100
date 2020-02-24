# This program advises the user of what insurance best suites their
# life style based on the info they input.

# Global Constant
PERCENTAGE = .80

# Main Function
def main():
    # Get the replacement cost from the user
    replacement_cost = float(input('What is the replacement cost? '))
    # Calulate Insurace Cost
    insurance = replacement_cost * PERCENTAGE
    # Call to show_insurance function
    show_insurance(insurance)

# Show_insurance function
def show_insurance(insurance):
    print('The cost of your insurance should be at least $', \
          format(insurance,'.2f'),sep='')

# Call to main function
main()
