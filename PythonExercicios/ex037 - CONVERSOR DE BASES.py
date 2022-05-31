from time import sleep
print('\n\33[1;33m')
print('>'*11,'CONVERSÃO NUMERICA','<'*11)
print('\n\33[m')
n = int(input('\33[1;37mInsira o numero (INTEIRO) \n para conversão: '))
print('\n')
b = int(input('Digite o numero para escolher a base:\33[m\n \33[1;35m1-BINARIO\n \33[1;36m2-OCTAL\n \33[1;34m3-HEXADECIMAL \n\33[1;37mDigite sua escolha: '))
sleep(.5)
print('\n\nAGUARDE ENQUANTO FAÇO A CONVERSÃO...\n\n')
sleep(1)
if b==1:
    print('\33[1;35mO numero {} em BINARIO fica: {}'.format(n, format(n, 'b')))
    # coódigo do prof >>> print('{} convertido para binario é igual a {}'.format(n, bin(n)[2:]))
elif b==2:
    print('\33[1;36mO numero {} em OCTANO fica: {}'.format(n, format(n, 'o')))
    # coódigo do prof >>> print('{} convertido para binario é igual a {}'.format(n, oct(n)[2:]))
else:
    print('\33[1;34mO numero {} em HEXADECIMAL fica: {}'.format(n, format(n, 'x')))
    # coódigo do prof >>> print('{} convertido para binario é igual a {}'.format(n, hex(n)[2:]))
print('\n\33[1;33m')
print('>'*18,'FIM','<'*19)
print('\33[m')

