def main():
    a = int(input('What is the first number? '))
    b = int(input('What is the second number? '))
    total = sum(a,b)
    print('The total of the numbers is', total)

def sum(num1, num2):
    result = num1 + num2
    return result

main()
