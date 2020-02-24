# This program displays 2 random numbers that are to be added and
# program will allow the student to enter the answer and if
# it is correct a message should congrats. If it is wrong then
# it should display the correct answer.

# Import Random
import random

# Main Function
def main():
    # Get the numbers
    num_1 = random.randint(1,100)
    num_2 = random.randint(1,100)
    print(num_1, '+', num_2)
    answer(num_1,num_2)

def answer(num_1,num_2):
    your_answer = int(input('What is the total?: '))
    answer = num_1 + num_2
    display(num_1,num_2,your_answer,answer)

def display(num_1,num_2,your_answer,answer): 
    if your_answer == answer:
        print('Congratulations that is correct!')
    else:
        print('Sorry the answer was',answer)
        
# Call to Main
main()
