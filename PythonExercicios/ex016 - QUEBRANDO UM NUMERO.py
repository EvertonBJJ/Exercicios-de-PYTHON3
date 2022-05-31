# IMPORTANDO O MODULO
import math
numero = float(input('Insíra um numero: '))
print('A parte inteira do numero {} é o {}!'.format(numero, math.trunc(numero)))

# IMPORTANDO SOMENTE A FUNÇÃO
print('\n')
from math import trunc
numero = float(input('Insira um numero: '))
print('A parte inteira do numero {} é o {:.0f}!'.format(numero, trunc(numero)))

# SEM IMPORTAR MODULO
print('\n')
numero = float(input('Insira um numero: '))
print('A parte inteira do numero {} é o {:.0f}!'.format(numero, int(numero)))
