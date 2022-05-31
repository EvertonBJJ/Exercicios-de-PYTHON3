# IMPORTANDO MODOLO
import math
a = float(input('Insira o angulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('\nSeno de {:.2f}° é {:.2f}\nCosseno de {:.2f}° é {:.2f}\nTangente de {:.2f}° é {:.2f}'.format(a, s, a, c, a, t))

# IMPORTANDO SOMENTE FUNÇÕES
print('\n')
from math import radians, cos, sin, tan
a = float(input('Digite o ângulo: '))
ar = radians(a)
c = cos(ar)
s = sin(ar)
t = tan(ar)
print('\nO SENO de {:.2f} é {:.2f}\nO COSSENO de {:.2f} é {:.2f}\nA TANGENTE de {:.2f} é {:.2f}'.format(a, c, a, s, a, t))
