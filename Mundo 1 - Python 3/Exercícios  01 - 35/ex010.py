## Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira 
# e mostre quantos dólares ela pode comprar.

dinheiro = float(input('Quanto de dinheiro há em sua carteira? '))
conversao = dinheiro / 3.66

print(f'Você possui R${dinheiro:.2f} e seu valor em dolares será de ${conversao:.2f}')