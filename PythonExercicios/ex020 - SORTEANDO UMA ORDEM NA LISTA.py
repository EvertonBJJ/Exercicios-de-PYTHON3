from random import shuffle
a = str(input('Insira o nome do primeiro aluno: '))
b = str(input('Insira o nome do segundo aluno: '))
c = str(input('Insira o nome do terceiro aluno: '))
d = str(input('Insira o nome do quarto aluno: '))
l = [a, b, c, d]
shuffle(l)
print('A ordem de apresentação será:')
print(l)
