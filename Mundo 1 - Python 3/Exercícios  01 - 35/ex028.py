## Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e 
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

num = random.randint(0,5)
numero_esolhido = int(input('Escolha um número entre 0 e 5 '))

if num == numero_esolhido:
    print(f'Parabéns, você acertou, o computador escolheu {num} e você escolheu {numero_esolhido}')
else:
    print(f'Você errou, o computador escolheu {num} e você {numero_esolhido}')

    