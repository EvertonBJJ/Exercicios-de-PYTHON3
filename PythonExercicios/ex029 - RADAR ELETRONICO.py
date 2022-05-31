from time import sleep

print('\33[1;33m/'*42)
print('{::^42}'.format('RADAR'))
print('/'*42)
print('\n\33[m')
n1 = float(input('\33[1;34m Qual a velocidade do veiculo? '))
sleep(1)
if n1 > 80:
    print('\33[m\n \33[1;31mMULTADO! O limite de velocidade é 80km/h.\n  O valor da multa é R$ {:.2f}\33[m'.format((n1 - 80)*7.00))
else:
    print('\33[1;32m\n OK.\n  Você esta no limite\n  de velocidade de 80km/h.\33[m')
print('\33[1;33m\n')
print('/'*42)
print('{::^42}'.format(''))
print('/'*42)
print('\n\33[m')
