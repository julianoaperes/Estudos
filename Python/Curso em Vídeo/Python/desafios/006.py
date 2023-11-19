# Crie um algoritmo que leia um número e mostr o seu dobro, triplo e raiz quadrda

n =float(input('Escolha um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro do número escolhido é {:.2f}, o triplo é {:.2f} e sua raiz é {:.2f}.' .format(d, t, r))