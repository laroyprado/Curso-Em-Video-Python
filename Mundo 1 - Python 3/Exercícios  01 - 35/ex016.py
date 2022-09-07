## Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
num = float(input('Digite um número'))

print(f'número inteiro de {num} é {math.trunc(num)}')