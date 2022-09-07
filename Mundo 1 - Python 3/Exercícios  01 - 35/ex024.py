## Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Qual nome da sua cidade? ')).upper().split()
print ('SANTO' in cidade[0])


## OUU

cidade = str(input('Qual nome da sua cidade? ')).strip().upper
print((cidade[5]) == 'SANTO')