from time import sleep
from random import randint
pc = randint(0, 5)
print('\33[1;34m='*42)
print('\n')
print('{:-^42}'.format('ADIVINHE O NÚMERO'))
print('\n')
print('='*42)
print('\33[m\n')
sleep(0.5)
print('\33[1;33m VOU PENSAR EM UM NUMERO DE 0 A 5,\n  TENTE ADIVINHAR!')
print('\33[m\n\33[1;34m')
sleep(1)
print('-'*42)
print('\33[m')
print('\n \33[1mPENSANDO')
sleep(0.3)
print(' .')
sleep(0.3)
print(' .')
sleep(0.3)
print(' .')
sleep(0.3)
print('\n')
j = int(input(' PRONTO. \n  AGORA, ADIVINHE O NUMERO QUE PENSEI: '))
sleep(1)
print('\n')
if j==pc:
   print('\33[1;32m PARABÉNS, VOCÊ ACERTOU !!! O NÚMERO É {}\33[m'.format(pc))
else:
   print('\33[1;31m VOCÊ ERROU !!! O NÚMERO QUE PENSEI É {}\33[m'.format(pc))
print('\n')
sleep(1)
print('\33[1;34m{:-^42}\n\33[m'.format('FIM'))
