
from datetime import date
print('\33[1;33m''='*12,'CONFEDERAÇÃO NACIONAL DE NATAÇÃO','='*12,'\33[m\n')
nam = str(input('\33[34mInsira o nome do atleta: ')).strip().lower().capitalize()
ano = int(input('Digite o ano de nascimento: \33[m'))
cat = date.today().year-ano
print('\33[36m')
if cat <= 9:
  print(f'O atleta {nam} tem {cat} anos e pertence a categoria MIRIM!')
elif cat <= 14:
  print(f'O atleta {nam} tem {cat} anos e pertence a categoria INFANTIL!')
elif cat <= 19:
  print(f'O atleta {nam} tem {cat} anos e pertence a categoria JUNIOR!')
elif cat <= 20:
  print(f'O atleta {nam} tem {cat} anos e pertence a categoria SÊNIOR!')
else:
  print(f'\nO atleta {nam} tem {cat} anos e pertence a categoria MASTER!')
print('\33[m')
print('\33[1;33m''{:-^55}'.format('FIM'),'\33[m')
