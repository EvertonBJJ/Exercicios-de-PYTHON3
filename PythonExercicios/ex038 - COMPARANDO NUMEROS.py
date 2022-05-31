from time import sleep
print('\33[1;32m')
print('_'*46)
print('{:-^46}'.format('COMPARANDO VALORES'))
print('_'*46)
print('\33[m')
a = int(input('\33[1;31m Digite o primeiro valor inteiro: \33[m'))
b = int(input('\33[1;34m Digite o segundo valor inteiro: \33[m'))
sleep(.5)
print('\n\33[1;32m Analizando...\33[m\n')
sleep(.5)
if a > b:
    print('\33[1;31m O primeiro valor ({}) é o maior!\33[m'.format(a))
elif b > a:
    print('\33[1;34m O segundo valor ({}) é o maior!\33[m'.format(b))
else:
    print('\33[7m Não existe valor maior.\n  Os dois são iguais!\33[m')
print('\33[1;32m')
print('_'*46)
print('{:-^46}'.format('FIM'))
print('_'*46)
print('\33[m')