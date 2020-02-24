# This program is to that tells the consumer
# the subtotal of the price of five iteams
# and it calculates the sales price
# and calculates the total price.

# Get the price of the five items

item_1 = float(input('Enter the price of the first item '))
item_2 = float(input('Enter the price of the second item '))
item_3 = float(input('Enter the price of the third item'))
item_4 = float(input('Enter the price of the fourth item '))
item_5 = float(input('Enter the price of the fifth item '))

# Calculate the subtotal
subtotal = item_1 + item_2 + item_3 + item_4 + item_5

# Calculate the sales tax
sales_tax = subtotal * 0.07

# Calculate the total
total = subtotal + sales_tax

print('The subtotal is $',\
      format(subtotal, '.2f'))
print('The sales_tax is $', \
      format(sales_tax, '.2f'))
print('Total is $', \
      format(total, '.2f'))
               
