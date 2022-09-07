## Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite aqui o seu salário R$'))
aumento = salario + (salario * 0.15)
print(f'Seu salario é de R${salario:.2f}, com um aumento de 15% ele aumentará R${aumento-salario:.2f}, ficando então um total de R${aumento:.2f}')