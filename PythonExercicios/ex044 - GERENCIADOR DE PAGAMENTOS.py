print('\n')
print(f'\33[1;35m{" LOJA DO INDIÃO":-^40}\33[m')
print('\n')

preco = float(input('\33[1;32mQual o preço do produto? R$ '))

print('''\nFormas de pagamento:
 1 - À VISTA: Dinheiro/Cheque
 2 - À VISTA: C. CRÉDITO
 3 - PARCELADO C. CRÉDITO''')
cond = int(input('Selecione a forma de pagamento: \33[m'))

desc1 = 0.10
desc2 = 0.05
desc3 = 0.00
juros = 0.20
if cond == 1:
    print('O valor final produto é R$ {:.2f}'.format(preco - (preco * desc1)))
elif cond == 2:
    print('O valor final do produto é R$ {:.2f}'.format(preco - (preco * desc2)))
elif cond == 3:
    vzs = int(input('\33[1;32mQual a quantidade de parcelas? \33[m'))
    if vzs == 2:
        print('\nO valor final do produto é R$ {:.2f}\n Ficam {} parcelas de R$ {:.2f}'
              .format(preco - (preco * desc3), vzs, (preco - (preco * desc3)) / vzs))
    else:
        print('\nO valor final do produto é R$ {:.2f}\n Ficam {} parcelas de R$ {:.2f}'
              .format(preco + (preco * juros), vzs, (preco + (preco * juros)) / vzs))
print(f'\n'*2,f'{"OBRIGADO":-^40}')
