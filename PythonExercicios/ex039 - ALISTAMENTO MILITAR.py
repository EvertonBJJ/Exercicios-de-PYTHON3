from datetime import date
print('\n')
print('\33[1;34m{:=^44}\33[m'.format('ALISTAMENTO MILITAR'))
ano = int(input('\n\33[1;33mQual seu ano de nascimento? \33[m'))
age = date.today().year-ano
if age < 18:
    print(f'\n\33[1;3;400mAinda faltam {18-age} anos para você se alistar!\33[m')
    print(f'\n\33[1;3;400mSeu alistamento será em {ano+18}!\33[m')
elif age== 18:
    print('\n\33[1;32mVocê precisa se alistar este ano!')
else:
    print(f'\33[1;31mVocê devia ter se alistado há {age-18} anos atrás!')
    print(f'\n\33[1;3;400mSeu alistamento foi em {ano + 18}!\33[m')
print('\n\33[1;34m{:=^44}\33[m'.format('FIM'))
