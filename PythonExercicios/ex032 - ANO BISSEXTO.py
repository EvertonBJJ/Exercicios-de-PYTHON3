from datetime import date
print('\n')
a = int(input('\33[1;37mDigite o ano que quer consultar!\n Caso queira consultar o ano atual,\n  digite 0! \33[m'))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('\33[1;32mO ano ',a,' é BISSEXTO!\33[m')
else:
    print('\33[1;31mO ano ',a,' NÃO é bissexto!\33[m')
print('\n')