# This program will display the first five lines of the file
# contents

def main():
    # prompt the user to write the file name
    fileName = input('Enter the file name: ')

    # Open the file requested
    infile = open(fileName,'r')

    # Priming Read
    line = infile.readline()
    counter = 1

    # Read and display the first five line
    while line !='' and counter <=5:
        # Strip '\n'
        line = line.rstrip('\n')
        print(line)
        line = infile.readline()
        counter += 1

    infile.close()
main()
        
