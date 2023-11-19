# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais foi alugado e calcule o preço a pagar sabendo que 
# o carro custa R$60,00 por dia e R$0,15 por quilometro. 

d = int(input('Insira a quantidade de dias de aluguel: '))
km = float(input('Insira a quantidade de quilômetros rodados no período: '))
va = 60 * d
vkm = 0.15 * km 
print('O valor total a ser cobrado pelas diárias é de {:.2f} e o custo total da quilometragem rodada é de {:.2f}'.format(va, vkm))
