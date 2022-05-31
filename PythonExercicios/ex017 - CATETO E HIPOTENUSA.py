# MODO MANUAL S/ MODULO
co = float(input('Insira a medida do cateto oposto: '))
ca = float(input('Insira a medida do cateto adjacente: '))
h = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa do triangulo é {:.2f}!'.format(h))
print('\n')
# MODO MANUAL C/ MODULO
from math import sqrt
co = float(input('Insira a medida do cateto oposto: '))
ca = float(input('Insira a medida do cateto adjacente: '))
h = sqrt(pow(co, 2) + pow(ca, 2))
print('A hipotenusa do triangulo é {:.2f}!'.format(h))
print('\n')

# MODO AUTOMATICO
from math import hypot
co = float(input('Insira a medida do cateto oposto: '))
ca = float(input('Insira a medida do cateto adjacente: '))
h = hypot(co, ca)
print('A hipotenusa do triangulo é {:.2f}!'.format(h))
