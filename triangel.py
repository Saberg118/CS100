# This program will print an inverted triangle
# using seven rows.

# iterate over the rows
for row in range(7):
    for col in range(7,row,-1):
        print('*', end='')

        # go to the next row
    print()
