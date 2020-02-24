# Global Constant
STATE_TAX_RATE = 0.08
COUNTRY_TAX_RATE = 0.025

# Main Function
def main():
    # Get the purchase price from the user
    purchase = float(input('Enter the amount of the purchase: '))
    # Calculations
    state_tax = purchase * STATE_TAX_RATE
    country_tax = purchase * COUNTRY_TAX_RATE
    total_tax = state_tax + country_tax
    total_sale = purchase + total_tax
    # Call to display function
    display(purchase,state_tax,country_tax,total_tax,total_sale)

# Display funtion
def display(purchase,state_tax,country_tax,total_tax,total_sale):
    print('Purchase Amount:', format(purchase,'.2f'))
    print('State Tax:', format(state_tax,'.2f'))
    print('Country Tax:', format(country_tax,'.2f'))
    print('Total Tax:', format(total_tax,'.2f'))
    print('Total Sale:', format(total_sale,'.2f'))

# Call to main function
main()
