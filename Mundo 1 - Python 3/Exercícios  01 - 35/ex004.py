## Exercício Python 4: Faça um programa que leia algo pelo teclado e
## mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite algo ')

print('Seu tipo é', type(a))
print('É alpha númerico?', a.isalnum())
print('Só tem espaço?', a.isspace())
print('Está em formato título?', a.istitle())
print('Está em letras minusculas?', a.islower())
print('Está em letras maisculas?', a.isupper())

