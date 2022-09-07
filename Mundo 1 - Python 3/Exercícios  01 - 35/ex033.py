## Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.


num1 = int(input('Coloque um número '))
num2 = int(input('Coloque um número '))
num3 = int(input('Coloque um número '))

menor = num1

if num2 < num1 and num2 < num3:
    menor = num2

if num3 < num1 and num3 < num2:
    menor = num3

print('O menor número é {}'.format(menor))


maior = num1

if num2 > num1 and num2 > num3:
    maior = num2

if num3 > num1 and num3 > num2:
    maior = num3

print('O maior número é {}'.format(maior))