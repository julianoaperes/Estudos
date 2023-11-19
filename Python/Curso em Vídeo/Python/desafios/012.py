# Faça o algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto. 

pb = float(input('Qual o valor preço bruto do prdouto: '))
pd =(pb - (5 / 100) * pb)
print('O valor do produto com desconto de 5% é de: {}' .format(pd))
