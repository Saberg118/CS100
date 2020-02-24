# This program get the number of seats sold by each class and
# calculates the income generated from the ticket sales

# Global Constants
CLASS_A = 20
CLASS_B = 15
CLASS_C = 10

# Main Function
def main():
    # Get number of seats sold per each class from user
    seatA = int(input( "How many seats were sold in Class A: "))
    seatB = int(input( "How many seats were sold in Class B: "))
    seatC = int(input( "How many seats were sold in Class C: "))
    # Calculate income generated
    income = (CLASS_A * seatA) + (CLASS_B * seatB) + (CLASS_C * seatC)
    # Call to show_income
    show_income(income)

# Show_income Functions
def show_income(income):
    # Display income generated
    print("The income generated from the sales of the seats is $", \
          format(income,'.2f'),sep='')


# Call to main function          
main()   
