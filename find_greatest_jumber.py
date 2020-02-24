# This program will accept two numbers from the user
# and determines which number is the larger one.

# Main function
def main():
    # Get the numbers from the user
    num1 = int(input('What is your first number? '))
    num2 = int(input('What is your second number? '))

    # Find and display the max number
    print('The maximum number is', maximum(num1,num2))
    
# Definition of maximum(num1,num2)   
def maximum(num1,num2):
   # Find out which of the two numbers is the largest
   if num1 > num2:
       return num1 # Number one is the largest 
   elif num1 < num2:
       return num2 # Number two is the largest 
   else:
       print('The two number are equal to each other')

# Call the function
main()
        
