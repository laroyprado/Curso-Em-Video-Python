## Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

## – O nome com todas as letras maiúsculas e minúsculas.

## – Quantas letras ao todo (sem considerar espaços).

## – Quantas letras tem o primeiro nome.

nome = str(input('Qual o seu nome? '))
print(f'Seu nome com todas as letras maiúsculas {nome.upper()}')
print(f'Seu nome com todas as letras minúsculas {nome.lower()}')
print(len(nome), 'Letras')
nome_separado = nome.split()
print(f'O seu primeiro nome é {nome_separado[0]}')