## Exercício Python 35: Desenvolva um programa que leia o comprimento de
#  três retas e diga ao usuário se elas podem ou não formar um triângulo.



r1 = int(input('Insira a medida de um dos lados do triângulo '))
r2 = int(input('Insira a medida de um dos lados do triângulo '))
r3 = int(input('Insira a medida de um dos lados do triângulo '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('É um triangulo')
else:
    print('Isso não é um triângulo')