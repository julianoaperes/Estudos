# Faça um programa que leia o comprimento do cateto oposto e do
# cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.


co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
h = (co ** 2 + ca **2) ** (1/2)
print("A hipotenusa é igual a: {:.2f}" .format(h))
