# This program asks the user for the number of fat grams and
# carb grams that they consume in a day. Then it calculates the
# number of calories that result from the fat and carbs.

# main function
def main():
    # Get fat and carb grams
    fat_grams = int(input('Grams of fat consumed daily?: '))
    carb_grams = int(input('Grams of carbs consumed daily?: '))
    # call to calc funtion
    calc(fat_grams,carb_grams)

def calc(fat_grams,carb_grams):
    # calculate caloreis of fat and carbs
    calories_fat = fat_grams * 9
    calories_carbs = carb_grams * 4
    # call to display function
    display(fat_grams,carb_grams,calories_fat,calories_carbs)

# display function    
def display(fat_grams,carb_grams,calories_fat,calories_carbs):
    # Show calories of fat and carbs
    print('The number of calories consumed from fat is', \
          format(calories_fat,'.2f'))
    print('The number of calories consumed from carbs is',\
          format(calories_carbs,'.2f'))

# Call to main
main()
