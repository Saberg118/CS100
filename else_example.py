# adding optional else clause

try:
    num = float(input('Enter a number: '))

except ValueError:
    print('That was not a number')

else:
    print('You have entered the number:' , num)
