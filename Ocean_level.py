# This program displays the Ocean level
# through years 0 through 25


print('Years \t\t Ocean levels')
print('___________________________')

Ocean_level = 0  
for year in range(1,26,1):
    Ocean_level += 1.6
    print(format(year, '.2f'),'\t\t',format(Ocean_level,'.2f'), 'millimeters')
          
