# This program is a guessing number games that gives feedback to the
# user wither the number they guessed as too high or too low and
# then will be able to try again until they get the number.

import random

# Display instructions
print("""Welcome to the "Guess My Number"
I'm thinking of a number between 1 and 100.
Try to guess it in a few attempts as possible.
Are you ready?
Press Enter to Begin.""")

# Set the initial value
number = random.randint(1,100)

guess = int(input('What is your guess?: '))

tries = 1

# Guessing loop

while guess!= number:
    if guess > number:
        print("""The number you have guessed is too high!
Try guessing a lower number.""")
    else:
        
        print("""The number you have guessed is too low!
Try guessing a higher number.""")

    guess = int(input("Ready to try again?"))

    tries += 1

print("You've got the right number! It was", number)
print("It took you",tries,"try(ies)")
