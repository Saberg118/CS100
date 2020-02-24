# Create a number file
import random
myfile = open('number.txt', 'w')
for count in range (500):
    number = random.randint(1,500)
    myfile.write(str(number) + '\n')
myfile.close()

# Open the file
myfile = open('number.txt', 'r')

# Read and display the files content
for line in myfile:
    number = int(line)
    print(number)

# Close the file
myfile.close()
