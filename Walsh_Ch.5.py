# This program will calculate teh future value of a user's account when
# the user gives the current account value, monthly interest rate, and
# months that teh money will be left in that account.

# Main function
def main():
    # Call to get_info function
    get_info()

# Get_info function
def get_info():
    # Get the present value
    P = float(input('What is the present value of your account? :$ '))
    # Display instruction
    print('In decimal value')
    # Get the monthly interest rate
    i = float(input('What is the monthly interest rate?:'))
    # Get the time in months
    t = int(input('How many months will that money be left in the account?: '))
    # Call to calcuations
    calc(P,i,t)

# Calc funtion
def calc(P,i,t):
    # Calculate Future Cost
    F = P * (1 + i)** t
    # Call to display function
    display(P,i,t,F)

# Display Function
def display(P,i,t,F):
    # Show present value
    print('The money currently in the account is $', \
          format(P,',.2f'),sep = "")
    # Show monthly interest rate
    print('The monthly interest rate is', i * 100, '%')
    # Show the time in months
    print('It will be in there for',t,'months')
    # Show the future value
    print('The future value of the account is $', \
          format(F, ',.2f'),sep = "")

# Call to main function
main()
    
