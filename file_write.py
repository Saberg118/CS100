# This program writes three lines of data to a file

# Main Function
def main():
    # Open file named philosophers.txt.
    outfile = open('philosophers.txt.', 'w')

    # Write the names of teh three philosophers
    # to the file
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    # Close the file
    outfile.close()

# Call to the main function
main()
    
                   
