# This program will display the pay a person earns
# if paid a penny on the first day and they pay
# doubles each day afterwards

# Initailize the accumalator
total = 0.0
pennies_per_day = 1

# Get the input from the user
number_of_days = int(input('Enter the number of days: '))

# Print column headings
print('Salary\t\t\Pennies')
print('______________________________')

# for loop
for day in range (1,number_of_days +1):
    print(day,'\t$',float(pennies_per_day/100))
    total += pennies_per_day
    pennies_per_day *= 2

print('The total salary for', number_of_days, 'days is: $', float(total/100))
