s=float(input('Qual seu salario? '))
if s>1250:
    sn=s*0.1+s
if s<=1250:
    sn=s*0.15+s
print('Seu novo salario será R$ {:.2f}'.format(sn))
