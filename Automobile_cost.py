# This program asks the user for the monthly costs of their automobile
# such as the  loan payment, insurance, gas, oil, tires, and maintance.
# This program will display the monthly copst of thes44e expenses and
# calculate the total annual cost of these expenses.

# Global constant
YEAR = 12

# Main Function
def main():
    loan_payment = float(input('How much do you pay monthly for loan payment '))
    insurance = float(input('How much do you pay monthly for insurace '))
    gas = float(input('How much do you pay monthly for gas '))
    oil = float(input('How much do you pay monthly for oil '))
    tires = float(input('How much do you pay monthly for tires '))
    maintenance = float(input('How much do you pay tmonthly for maintenance '))
    # Calc monthly cost
    monthly_cost = insurance + gas + oil + tires + maintenance + loan_payment
    # Calc annual cost
    annual_cost = (insurance + gas + oil + tires + maintenance + loan_payment) * YEAR
    # Call to display_cost
    display_costs(loan_payment, insurance, gas, oil, tires, maintenance,annual_cost, monthly_cost)
    
   
# Display costs function
def display_costs(loan_payment, insurance, gas, oil, tires, maintenance,annual_cost, monthly_cost):
    print('Monthly loan payment cost is  $',format(loan_payment,',.2f'),sep='')
    print('Monthly insurance cost is  $',format(insurance,',.2f'),sep='')
    print('Monthly gas cost is  $',format(gas,',.2f'),sep='')
    print('Monthly oil cost is  $',format(oil,',.2f'),sep='')
    print('Monthly tires cost is  $',format(tires,',.2f'),sep='')
    print('Monthly maintenance cost is  $',format(maintenance,',.2f'),sep='')
    print('Monthly total cost is  $',format(monthly_cost,',.2f'),sep='') 
    print('Your annual cost of all these expeneses is  $',format(annual_cost,',.2f'),sep='')

# Call to main
main()

    
