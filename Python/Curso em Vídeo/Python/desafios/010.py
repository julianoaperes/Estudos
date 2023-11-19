# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar

r = float(input('Quantos reais você tem em sua carteira: '))
usd = r / 3.27
print('De acordo com a cotação mais atual, você conseguirá comprar {} dolares' .format(usd))
