print('\n')
print('{:-^70}'.format('MEDIA'))
name = str(input('\nQual o nome do aluno? ')).strip().lower().title()
note1 = float(input('\nInsira a primeira nota: '))
note2 = float(input('Insira a segunda nota: '))
mean = (note1+note2)/2
if mean <= 5.0:
    print(f'\nO aluno {name} teve média {mean} e foi REPROVADO!!!')
elif 5.0 < mean < 6.9:
    print(f'\nO aluno {name} teve média {mean} e esta de RECUPERAÇÃO')
else:
    print(f'\nO aluno {name} teve média {mean} e foi APROVADO!!!')
print('\n{:-^70}'.format('FIM'))
