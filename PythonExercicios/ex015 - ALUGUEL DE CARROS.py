print('')
print('='*22,'\n===ALUGUEL DE CARRO===')
print('='*22)
d = int(input('\nPor quantos dias o \ncarro foi alugado? '))*60
k = float(input('Quantos kilometros \nele rodou? '))*.15
a = d + k
o = str('OBRIGADO')
print('\nO preço total a \npagar pelo aluguel \né de R$ {:.2f}.'.format(a))
print('\n{:>22}!'.format(o))
print('=' * 23)
