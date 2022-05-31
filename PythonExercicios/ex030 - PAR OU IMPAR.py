from time import sleep
print('\33[1;36m\n')
print('○●'*21)
p = ' PAR OU ÍMPAR '
print('{:=^42}'.format(p))
print('○●'*21)
sleep(1)
n = float(input('\33[m\n\33[1;33m Digite um numero: '))
m = (n%2)
if m==0:
    print('\n  O número {} é PAR !!!'.format(n))
else:
    print('\n O numero {} é ÍMPAR !!!'.format(n))
sleep(1)
print('\33[m\n\33[1;36m{:=^42}\n\n\33[m'.format(' FIM '))


