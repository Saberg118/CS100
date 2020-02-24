# This program asks the user to enter a series of possitive numbers
# and ends the loop when the person enters a negative number.
# Then the program will calculate the total of sum of all the
# numbers entered.

# Initialize the accumulator
total = 0
number = 1

# The while loop
while number > 0:
    number = int(input('Please input a possitive number: '))
    if number > 0:
        total += number
print('The total of the number you entered is',total)
     
    

