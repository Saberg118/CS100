# Getting the exception arguement

try:
    num = float(input('Enter a number: '))

except ValueError as argument:
    print(" That is not a number. Python says:")
    print(argument)
