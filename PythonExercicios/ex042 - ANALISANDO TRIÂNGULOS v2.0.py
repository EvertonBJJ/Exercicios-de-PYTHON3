print('\33[1;35m\n{:=^44}\33[m'.format('ANALISANDO TRIÂNGULOS'))
print('\n')
l1 = float(input('Insira o primeiro lado: '))
l2 = float(input('Insira o segundo lado: '))
l3 = float(input('Insira o Terceiro lado: '))
print('\n')
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1 and l1 == l2 == l3 :
    print('\33[1;32mOs segmentos acima PODEM FORMAR\n um TRIÂNGULO e este é EQUILÁTERO!\33[m')
elif l1+l2>l3 and l1+l3>l2 and l2+l3>l1 and l1==l2 or l1==l3 or l2==l3 :
    print('\33[1;32mOs segmentos acima PODEM FORMAR\n um TRIÂNGULO e este é ISÓSCELES!\33[m')
elif l1+l2>l3 and l1+l3>l2 and l2+l3>l1 and l1!=l2 and l1!=l3 and l2!=l3 :
    print('\33[1;32mOs segmentos acima PODEM FORMAR\n um TRIÂNGULO e este é ESCALENO!\33[m')
else:
    print('\33[1;31mOs segmentos acima NÃO PODEM FORMAR\n um TRIÂNGULO!\33[m')
print('\n\33[1;35m{:=^44}\33[m'.format('FIM'))

# código do prof >>>
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Os segmentos acima PODEM FORMAR um TRIÂNGULO', end="")
    if l1 == l2 == l3 :
        print('Esse TRIÂNGULO é EQUILÁTERO!')
    elif l1 != l2 != l3 != l1:
        print('Esse TRIÂNGULO é ESCALENO!')
    else:
        print('Esse TRIÂNGULO é ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um TRIÂNGULO!')
