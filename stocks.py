# This program calculates the net loss or gain
# in profit from buying and selling stocks.

# Declare constants
number_shares = 2000
buy_price = 40.00
commission_rate = 0.03
sell_price = 42.75

# Calculate the purchase price
purchase = number_shares * buy_price

# Calculate the commission paid for buying stock
commission1 = purchase * commission_rate

# Calculate total
total = purchase + commission1

# Calculate price sold
sold = number_shares * sell_price

# Calculate the commission paid for selling stock
commission2 = sold * commission_rate

# Calculate the sold price
sold_price = sold - commission2

# Calculate net loss or gain
net = sold_price - total

# Display purchase price
print('The amount paid for the stock is $', \
      format(purchase,',.2f'))

# Display buying commission price
print('The commission paid for buying stock is $', \
      format(commission1,',.2f'))

# Display selling price
print('The amount sold for is $', \
      format(sold,',.2f'))

# Display selling commission price
print('The commission paid for selling stock is $', \
      format(commission2,',.2f'))

# Display net loss or gain
print('The net gain or loss is $', \
      format(net,',.2f'))


