# This program calulate the average of all the numbers stored in
# in the number.txt file.

def main():
    # set the counter
    counter = 0
    
    # set the accumulator
    total = 0
    try:
        # open the number.txt. file.
        infile = open('number.txt', 'r')
        for line in infile:
            counter = counter + 1
            number = float(line)
            total += number
        # Close the file.
        infile.close()
        #Calculate the average
        average = total / counter
        # Display the average
        print('The average of your numbers is: ',average)

    except IOError:
            print('An error occured trying to read the file.')

    except ValueError:
            print('Non-numeric data found in file.')
            
# Call to main
main()

    

    

    
    
