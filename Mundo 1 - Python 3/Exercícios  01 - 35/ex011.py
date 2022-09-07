## Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e 
# a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

altura = float(input('Qual altura da parede? (Em Metros) '))
largura = float(input('Qual largura da parede?(Em Metros) '))
area = altura * largura
qnt_tinta = area / 2
print(f'A quantidade de litros de tinta necessário será de {qnt_tinta} Litros ')