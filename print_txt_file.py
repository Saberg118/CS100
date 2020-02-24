# This program reads and displays the contents
# of teh philosphers.txt file.

# Main function
def main():
    # Open a file named philosophers.txt file.
    infile = open('philosophers.txt', 'r')

    # Read the file's contents.
    file_contents = infile.read()

    # Close the file
    infile.close()

    # Print the data that was read into memory
    print(file_contents)

# Call to the Main Function
main()
