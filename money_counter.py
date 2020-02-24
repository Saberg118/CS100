# This program is a money counting game that works by gettings
# the user to input the number of pennies nickles dimes and
# quarters needed to make exactlya dollar and prints
# the result of their input.

# Assign money to values
PENNY = 0.01
NICKLE = 0.05
DIME = 0.10
QUARTER = 0.25

# Get the number of coins from the user.
P = int(input('How many pennnies?: '))
N = int(input('How many nickles?: '))
D = int(input('How many dimes?: '))
Q = int(input('How many quarters?: '))

# sum of pennies nickles dimes and quarters
# to obtain the total value
total_value = (P * PENNY) + (N * NICKLE) + (D * DIME) + (Q * QUARTER)

if total_value == 1.00:
    print("""Congradulations! You have made exactly $1.00.
You are a WINNER!!!""")
elif total_value > 1.00:
    print("""I'm sorry but that is not correct!
You are over $1.00.
You have LOST!""")
else:
    print("""I'm sorry but that is not correct!
You are under $1.00.
You have LOST!""")
