# This program tells the user
# how many points they have earned
# based on the number of books they bought

# Get the number of books from the user.
books = int(input('How many books did you buy this month?: '))

# Dispaly the number of points the user has earned.
if books == 0:
    print('You have earned 0 points')
elif books <= 2:
     print('You have earned 5 points')
elif books <= 4:
     print('You have earned 15 points')
elif (books <= 6) or (books == 7):
     print('You have earned 30 points')
else:
    (books == 8) or (books > 9)
    print('You have earned 60 points')


