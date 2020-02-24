
# This program will calculate the compound interest rate
# of Mrs. Loggie's bank account according to the infomation
# inputed by the user



# Get years and amount they are going to invest
years = int(input('How many years will you invest for?: '))
amount_invested = float(input('How much money are you going to invest?: '))
interest_rate =  float(input( 'What is the  interest rate?: '))

# Initialize accumulator
total = 0.0

# Make a table
print('Year \t\ Balance')
print('___________________')


# for loop
for years in range(1,years +1):
    # Calculate the balance interest paid
    interest = interest_rate * amount_invested
    amount_invested += interest
    total = amount_invested
    
    # Display table
    print(format(years,'.1f'),'\t\t',format(total,',.2f'))
    
    

