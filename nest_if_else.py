# This program asks for the length and width of two rectangles
# and comapares the areas and tells the user the result of
# its calculations.

# Get the length and width of the rectangles
length1 = int(input('What is the length  of the first rectangle? '))
width1 = int(input('What is the width of the second rectangle? '))

length2 = int(input('What is the length of the first rectangle? '))
width2 = int(input('What is the width of the first rectangle? '))

# Calculate the area
area1 = length1 * width1
area2 = length2 * width2

if area1 > area2:
    print('Rectangle 1 has the greater area.')
else:
    if area1 < area2:
        print('Rectangle 2 has the greater area')
    else:
        print('They both have the same area')
