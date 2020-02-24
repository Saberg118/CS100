# This program is to convert temperatures in
# Celsius to Fahrenheit.

# Get the Celsius temperature from the user.
C = float(input('The temperature in Celsius is? '))

# Calculate Celsius into Fahrenheit.
F = (9/5 * C) + 32

# Display the temperature in Fahrenheit.
print('The temperature is', \
      format(F,'.1f'),'degrees Fahrenheit')
