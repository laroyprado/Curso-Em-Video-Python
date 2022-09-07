## Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#  e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos Km foram percorridos? '))
dias = int(input('Quantos dias o carro ficou alugado? '))
valor_km = km * 0.15
valor_dias = dias * 60
valor_total = valor_km + valor_dias
print(f'O valor final será de R${valor_total:.2f}')
