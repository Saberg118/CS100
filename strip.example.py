# This program is an example of a strip

value = ' a line '

# Remove the left spaces
value1 = value.lstrip()
print('['+ value1 +']')

# Remove the right spaces
value2 = value.rstrip()
print('['+ value2 + ']')

# Remove the left and right spaces
value3 = value.strip()
print('[' + value3 + ']')
