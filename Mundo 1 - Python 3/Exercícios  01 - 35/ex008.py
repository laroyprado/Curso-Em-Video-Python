## Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro = float(input('Qual valor em metros? '))
cm = metro * 100
mm = metro * 1000
print(f'A medida escolhida em metros foi de {metro} metros, seu valor em cm é de {cm}centímetros e seu valor em mm é de {mm} milímetros')