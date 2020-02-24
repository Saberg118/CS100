# This programs keeps the running total of the amount of bugs
# collected during the 5 day loop.
total = 0

# Get the bugs collected for each day
for day in range(1, 6):
    print(' Enter the bugs collected on day',day)
    bugs = int(input())
    # Add bugs to total
    total = total + bugs

# Display the total bugs/
print('You have collected a total of',total,'bugs')
