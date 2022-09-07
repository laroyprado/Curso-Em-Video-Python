## Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
## em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite a frase ')).strip().lower()

print('a letra A aparece {} vezes'.format(frase.count('a')))
print('a letra A aparece na primeira vez em posição {}'.format((frase.find('a')+1)))
print('a letra A aparece na última vez vez em posição {}'.format((frase.rfind('a')+1)))
print(len(frase))