## Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual o preço do produto? '))
preco_atualizado = preco - (preco * 0.05)
print(f'O preço o produto é de R${preco:.2f}, porém com desconto de 5%, ele ficará em R${preco_atualizado:.2f}')