## Exercício Python 18: Faça um programa que leia um ângulo qualquer
#  e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Digite o ângulo por favor '))
seno = math.sin(math.radians(angulo))
print(f'O valor do seno de {angulo}º é {seno:.2f}')

coss = math.cos(math.radians(angulo))
print(f'O valor do cosseno de {angulo}º é de {coss:.2f}')

tg = math.tan(math.radians(angulo))
print(f'O valor da tangente de {angulo}º é de {tg:.2f}')