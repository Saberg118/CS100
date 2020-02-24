# This program is to find the interest rate of money in a bank

# Get desired value
F = float(input("Amount you want in your account"))

#Get annual interest rate
r = float(input("Annual interest rate"))

# Get  the number of years
n = float(input("How many year"))

# Calculate the amount needed to deposit
P = F/ (1.0 + r)**n

# Display the amount need to deposit
print('You will need to deposit $', \
      format(P,'.2f'))
