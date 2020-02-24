# This program keeps the running total of the expenses of the user
# and it will give the feedback wither or not the user stayed on
# their proposed budget or if they were over or under it.

total = 0.0 # initialize the accumulator

expense = 1.0 # initialize the while loop

# Get the budget amount from the user
budget = float(input('Enter your budget for the month. '))

# Get the total amount of expenses from the user
while expense != 0:
    expense = float(input("""Enter how much you have spent
or 0 to stop?"""))
    # Added to the total
    total += expense
# determine wither he is under or over or at their budget
# and display the result
print('Budget: $', format(budget,".2f"))
print('Expense: $', format(total,".2f"))

if budget > total:
    difference = budget - total
    print('You are $', format(difference, ".2f"),\
         'under your budget')
elif budget < total:
    difference = total - budget
    print('You are $', format(difference, ".2f"),\
          'over your budget')
else:
    print('You have stayed on budget')
    
