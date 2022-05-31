from time import sleep

print('\n\33[1;35m{:-^40}\33[m\n'.format('IMC'))
sleep(.3)
peso = float(input('Qual seu peso em quilos? '))
altura = float(input('Qual sua altura em metros? '))
imc = peso / altura ** 2
sleep(.3)
print(f'\n\33[1;34mO IMC dessa pessoa é de {imc:.1f}','\33[m')
if imc < 18.5:
    print('\33[1;33m Atenção! Você esta abaixo do peso!\33[m')
elif 18.5 <= imc < 25:
    print('\33[1;32m PARABÉNS!! Você está em seu peso ideal!\33[m')
elif 25 <= imc < 30:
    print('\33[1;33m Atenção! Você esta em sobrepeso!\33[m')
elif 30 <= imc < 40:
    print('\33[1;31m CUIDADO!! Você esta obeso!\33[m')
else:
    print('\n\33[1;30;41m CUIDADO!!! Você esta em OBSIDADE MÓRBIDA!\33[m')
sleep(.3)
print('\n\33[1;35m{:-^40}\33[m'.format('FIM'))
