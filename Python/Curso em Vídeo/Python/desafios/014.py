# Escreva um programa que converta uma temperatura digita em graus Celsius para F.

c = float(input('Informe a temperatura em °C: '))
f = ((9 * c) / 5) + 32
print('A temperatura de {:.2f}°C corresponde a {:.2f}F!'.format(c, f))
