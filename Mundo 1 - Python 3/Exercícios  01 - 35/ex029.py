## Exercício Python 29: Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual velocidade do carro? '))

if velocidade > 80:
    multa = 7 * (velocidade - 80)
    print(f'Você estava acima da velocidade, por isso foi aplicado uma multa, que sera de R${multa:.2f}')
else:
    print('Parabéns, você está na velocidade permitida')