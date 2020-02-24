# This program calculate the percentage of males and females
# in a given class.

# Get the number of girl in the class.
girls = int(input('How many females are in the class? '))

# Get the number of boys in the class.
boys = int(input('How many males are in the class? '))

# Calculate the number of students in the class
students = boys + girls

# Calculate the percentage of girls in the class.
percentage_of_girls = (girls / students) * 100

# Calculate the percentage of boys in the class.
percentage_of_boys = (boys / students) * 100

# Display the percentage of females in the class
print('The percentage or females in the class is', \
      format(percentage_of_girls, '.2f'),'%')

# Display the percentage of males in the class
print('The percentage or males in the class is', \
      format(percentage_of_boys, '.2f'),'%')
