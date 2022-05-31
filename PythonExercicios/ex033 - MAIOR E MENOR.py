a = float(input('Digite o primeiro numero: '))
b = float(input('Digite o segundo numero: '))
c = float(input('Digite o terceiro numero: '))
l = sorted([a, b, c])
print(f'O maior numero é {l[2]}!\nO menor numero é {l[0]}!')
#metodo Guanabara 
##menor
m = a
if b<a and b<c:
    m = b
if c<a and c<b:
    m = c
##maior
ma = a
if b>a and b>c:
    ma = b
if c>b and c>a:
    ma = c
print('O maior é',ma)
print('O menor é',m)
