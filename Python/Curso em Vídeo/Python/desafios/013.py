# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento. 

sb = float(input('Qual o salário bruto do funcionário: '))
sa = sb + (15 / 100) * sb
print('O novo salário do funcionário com o aumento passará a ser de: {}' .format(sa))
