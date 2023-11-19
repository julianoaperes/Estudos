n1 = int(input('Insira um valor: '))
n2 = int( input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2 
print('A soma é {}, \n o produto é {} e a divisão é {:.3f}.' .format(s, m, d), end=' ')
# Na mscara {:.3f}, o número 3 indica a quantidade de casas decimais a serem mostradas no resultado
# A letra f indica que o número é flutuante (float)
# end='', mostrará o resulta na sequência, ou seja, na mesma linha. Normalmente, os printis imprimiriam em linhas diferentes
# O print pode ser qubrado utilizando \n
print('A divisão inteira é {} e potência é {}.' .format(di, e))
