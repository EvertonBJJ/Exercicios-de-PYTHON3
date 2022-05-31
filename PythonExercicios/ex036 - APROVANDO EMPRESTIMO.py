from time import sleep
print('\n\33[1;36m')
print('{:=^42}'.format(' EMPRÉSTIMO - MINHA CASA MINHA DIVIDA '))
print('\33[m\n')
print('\33[33m')
c = float(input('Qual o valor da casa?: '))
s = float(input('Qual seu salario?: '))
p = int(input('Em quantas parcelas deseja pagar?: '))
sleep(.5)
print('\nANALIZANDO SUA SOLICITAÇÃO...\n')
print('\33[m')
sleep(1.5)
m = c/p
if m<(s*.3):
    print('\33[1;32m\n PARABENS!\n  SEU EMPRÉSTIMO FOI APROVADO!!!\n   Você ira pagar R${:.2f} por mês!\33[m'.format(m))
else:
    print('\33[1;31m QUE PENA!\n  Seu empréstimo foi NEGADO!\n   Tente novamente em breve!\33[m')
print('\n'*2)
print('\33[1;36m{:=^42}\33[m'.format(' OBRIGADO! '))
print('\n')