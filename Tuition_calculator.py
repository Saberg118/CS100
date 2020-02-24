# This program will display the projected semester tuition for the next 5
# years if tuition increases by 3%

# Initialize 
tuition = 8000

# Make a table

print('Years \t\t Tuition')
print('___________________________')

#for loop
for year in range(1,6):
    # Calculate tuition
    tuition *= 1.03
    # Display table
    print(format(year, '.2f'),'\t\t',format(tuition,'.2f'))
