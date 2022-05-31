from time import sleep
import emoji, random


obj = ("PEDRA :gem:", "PAPEL :page_facing_up:", "TESOURA :scissors:")
pe = "PEDRA :gem:"
pa = "PAPEL :page_facing_up:"
te = "TESOURA :scissors:"
r = ["\33[1;31m"]
g = ["\33[1;32m"]
y = ["\33[1;33m"]
b = ["\33[36m"]
p = ["\33[1;35m"]
x = ["\33[m"]

print(p[0])
print(f'{"JOKENPÔ":=^42}',x[0])
print('\n',b[0])
print('''Vamos jogar...
Escolha seu objeto:''')
print(emoji.emojize('0- {}'.format(pe), language='alias'))
print(emoji.emojize('1-{}'.format(pa), language='alias'))
print(emoji.emojize('2-{}'.format(te), language='alias'))
j = int(input('\nQual você escolhe? '))
pc = random.randint(0, 2)

print('\nOK. Vamos lá!')
sleep(.3)
print('\n JO...')
sleep(.3)
print('  KEN...')
sleep(.3)
print('   PÔ...')
sleep(.3)
print(emoji.emojize('\nJogador escolheu {}'.format(obj[j]), language='alias'))
print(emoji.emojize('O pc escolheu {}'.format(obj[pc]), language='alias'))
if j == pc:
    print(y[0],'\n  Empate!',x[0])
elif j == 1 and pc == 3 or j == 2 and pc == 1 or j == 3 and pc == 2:
    print(g[0],'\n  PARABÉNS! VOCÊ GANHOU!',g[0])
else:
    print(r[0],'\n  Que pena, você perdeu!',x[0])
print('\n',p[0])
print(f'{"FIM":=^42}')
print(x[0])