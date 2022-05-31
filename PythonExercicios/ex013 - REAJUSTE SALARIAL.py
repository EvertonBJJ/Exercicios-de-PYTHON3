print('\n *** NOVO SALÁRIO ***\n')
n = input('Qual o nome do funcionário? ')
s = float(input('Qual seu salário atual? R$ '))
print('\nO salário de {} com aumento é de R$ {:.2f} !'.format(n, s+(s*0.15)))
