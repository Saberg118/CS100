# This program will display the number of calories burned
# for 10,15,20,25,and 30 minutes.

print('Minutes\t\tCalories Burned')

print('____________________________')

# Use a for loop with the range functions with
# three arguments to display the calories burned.

for minutes in range(10,31,5):
    calories_burned = 4.2 * minutes
    print(minutes,'t\t',calories_burned)
