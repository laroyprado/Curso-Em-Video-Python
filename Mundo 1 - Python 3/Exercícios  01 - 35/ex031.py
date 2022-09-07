## Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
#  Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Qual a distância da viagem? '))

if distancia <= 200:
    preco_passagem = distancia * 0.50
    print(f'Sua viagem será de {distancia}KM, por isso o preço dela será de R${preco_passagem:.2f}')
else:
    preco_passagem = distancia * 0.45
    print(f'Sua viagem será de {distancia}KM, por isso o preço dela será de R${preco_passagem:.2f}')