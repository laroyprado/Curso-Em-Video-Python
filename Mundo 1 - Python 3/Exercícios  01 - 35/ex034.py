## Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
#  Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual o seu salário? '))

if salario > 1250:
    aumento = ( 0.10 * salario ) + salario
    print(f' Seu novo salário será de R${aumento:.2f}, seu antigo salário era de R${salario:.2f}. Você obteve um aumento de  R${aumento - salario :.2f}')

else:
    aumento = ( 0.15 * salario) + salario
    print(f'O seu salário será de R${aumento:.2f}, o seu aumento foi de  R${aumento - salario :.2f}')