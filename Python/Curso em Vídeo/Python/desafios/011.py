# Faça um programa que leia a largura e a altura de uma parede em metros. 
# Calcule sua área e a quantidade de tinta necessária para pintá-la. 
# Sabendo que cada litro de tinta pinta uma área de 2m2. 

lp = (float(input('Digite a largura da parede em metros(m): ')))
ap = (float(input('Digite a altura da parede em metros(m): ')))

a = lp * ap

print('Esta parede tem uma medida de {} metros quadrados. A quantidade, em litros, de tinta necessária para pintar essa parede será de: {} L' .format(a, a * 2))
