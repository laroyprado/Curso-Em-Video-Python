## Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#  Calcule e mostre o comprimento da hipotenusa.
import math
cat_oposto = float(input('Digite o cateto oposto '))
cat_adjacente = float(input('Digite o cateto adjacente '))
hipo = math.hypot(cat_oposto , cat_adjacente)
print(f'A hipotenusa será de {hipo:.3f}')
