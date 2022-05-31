print('\33[1;31m -\33[m'*42)
c1=float(input('\n\n\33[1;;mInsira o primeiro lado: '))
c2=float(input('Insira o segundo lado: '))
h=float(input('Insira o ultimo lado: '))
if c1+c2>h and c1+h>c2 and c2+h>c1:
    print('\33[1;32mOs segmentos acima PODEM FORMAR\n um TRIÂNGULO!\33[m')
else:
    print('\33[1;31mOs segmentos acima NÃO PODEM FORMAR\n um TRIÂNGULO!\33[m')
