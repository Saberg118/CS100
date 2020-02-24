# This program reads the contents of the friends.txt file
# one line at a time.

def main():
    # Open a file names friends.txt.
    infile = open('friends.txt','r')

    # Read three lines from the file.
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    # Strip the \n from each string.
    line1 = line1.rstrip()
    line2 = line2.rstrip()
    line3 = line3.rstrip()

    # Close the file
    infile.close()

    # Print the data that was read into memory.
    print(line1)
    print(line2)
    print(line3)

# Call the main function
main()
