name = str(input('Qual seu nome completo?: '))
nameok = name.strip()
print('Seu nome em letras maiúsculas: {} !'.format(nameok.upper()))
print('Seu nome em letras minúsculas: {} !'.format(nameok.lower()))
name1 = nameok.replace(' ','')
print('Seu nome todo possui {} letras!'.format(len(name1)))
name2 = nameok.split()
print('Seu primeiro nome possui {} letras!'.format(len(name2[0])))



