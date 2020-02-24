# This program is a color mixer that
# gets the user to pick two primary colors
# and results in a new color.

# Get the two primary colors from the user.
color1 = input('What is the first primary color? ')
color2 = input('What is the second primary color? ')

# Display the result of the colors combining.
if (color1 == "Red" and color2 == "Yellow") or \
   (color1 == "Yellow" and color2 == "Red"): 
    print('Orange')
elif (color1 == "Blue" and color2 == "Yellow") or \
     (color1 == "Yellow" and color2 == "Blue"):
    print('Green')
elif (color1 == "Red" and color2 == "Blue") or \
     (color1 == "Blue" and color2 == "Red"):
    print('Purple')
else:
    print('Those are not valid PRIMARY color!!')

