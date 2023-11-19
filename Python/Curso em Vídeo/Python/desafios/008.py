# Escreva um porgrama que leia um valor em metros e o exiba convertido em centímetros e milímetros

v = float(input('insira a media em metros (m): '))
c = v / 100
m = v / 1000
print('A medida convertida para centímetro é: {} cm.' .format(c))
print('A medida convertida para milimímetros é: {} mm.' .format(m))
