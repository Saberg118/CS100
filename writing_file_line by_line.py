# This program reads the contnets of the
# philosphers.txt file one line at a time.

# Main function
def main():
    # Open a file named philosphers.txt.
    infile = open('philosophers.txt', 'r')

    # Read three lines from the file.
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    # Close the file.
    infile.close()

    # Print the data that was read into memory
    print(line1)
    print(line2)
    print(line3)

# Call to main function
main()
