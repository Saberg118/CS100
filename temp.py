# This program displays the temperature
# for Celsius temperatures 0 through 20
# and caluclates it Farenheit equivlant

print('Celsius\t Farenheit')
print('______________________')

for C in range(0,21):
    Farenheit = (9/5) * C + 32
    print(format(C, '.2f'),'\t',format(Farenheit,'.2f'))
          
