print('\33[7m\n')
d = float(input('Qual a distancia da viagem em Km?: '))
if d <= 200:
    p = d * 0.50
    print('\n Sua passagem fica em R$ {:.2f} !'.format(p))
else:
    p = d * 0.45
    print('\n Sua passagem fica em R$ {:.2f} !'.format(p))
print('\n\33[m')