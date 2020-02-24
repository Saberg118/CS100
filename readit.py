print('Creating a text file with the write method')
text_file = open('read_it.txt','w')
text_file.write('Line1\n')
text_file.write('This is line 2.\n')
text_file.write('This makes this line 3.\n')
text_file.close()

print('\nReading the newly created file')
text_file = open('read_it.txt', 'r')
print(text_file.read())
text_file.close()

print('\nReading characters from the file.')
text_file = open('read_it.txt', 'r')
print(text_file.read(1))
print(text_file.read(5))
text_file.close()

print('\nReading one line at a time.')
text_file = open('read_it.txt','r')
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

print('\nStripping the new line from the readline program')
text_file = open('read_it.txt','r')
print(text_file.readline().rstrip())
print(text_file.readline().rstrip())
print(text_file.readline().rstrip())
text_file.close()

print('\nLooping through a file')
text_file = open('read_it.txt','r')
for line in text_file:
    print(line)
text_file.close()

print('\nStripping the new line from the loop output')
text_file = open('read_it.txt','r')
for line in text_file:
    print(line.rstrip())
text_file.close()

print('\nWriting numbers into a file')
import random
number_example = open('interger.txt', 'w')
for count in range (500):
    number = random.randint(1,500)
    number_example.write(str(number) + '\n')
number_example.close()

print('\nReading number from a file')
number_example = open('interger.txt', 'r')
sum = 0
for line in number_example:
    line = line.strip()
    number = int(line)
    sum += number
print('The sum is',sum)
number_example.close()
                         
