## Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

a1 = str(input('Qual nome do aluno '))
a2 = str(input('Qual nome do aluno '))
a3 = str(input('Qual nome do aluno '))
a4 = str(input('Qual nome do aluno '))

alunos = [a1, a2, a3, a4]
random.shuffle(alunos)
print(f'A ordem de apresentação será {alunos}')