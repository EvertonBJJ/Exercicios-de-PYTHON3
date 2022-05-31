# IMPORTANDO O MODULO
import random
a1 = input('Insira o nome do primeiro aluno: ')
a2 = input('Insira o nome do segundo aluno: ')
a3 = input('Insira o nome do terceiro aluno: ')
a4 = input('Insira o nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
s = random.choice(lista)
print('\nO aluno escolhido foi: {}!'.format(s))

# IMPORTANDO SOMENTE A FUNÇÃO
from random import choice
a = str(input('\nInsira o primeiro nome: '))
b = str(input('Insira o segundo nome: '))
c = str(input('Insira o terceiro nome: '))
d = str(input('Insira o segundo nome '))
lista = [a, b, c, d]
s = choice(lista)
print('\nO aluno escolhido foi o {}!'.format(s))