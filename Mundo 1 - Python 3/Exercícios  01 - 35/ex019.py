## Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido

import random

a1 = str(input('Qual nome do aluno '))
a2 = str(input('Qual nome do aluno '))
a3 = str(input('Qual nome do aluno '))
a4 = str(input('Qual nome do aluno '))

alunos = [a1, a2, a3, a4]
print(f'O aluno(a) escolhido apra apagar o quadro foi {random.choice(alunos)}')