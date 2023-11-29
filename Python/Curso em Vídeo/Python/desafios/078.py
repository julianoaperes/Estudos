# Faça um programa que leia 5 valores e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor assim como 
# suas posições na lista. 

valores = list()

for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

print(f'Os valores inseridos foram: {valores}.')

def maiorValor(valores):
    posicaoMaiorValor = valores[0]
    
    for val in valores:
        if val > posicaoMaiorValor: 
            posicaoMaiorValor = val
    return posicaoMaiorValor
    
print(f'O mair valor inserido foi: {maiorValor(valores)}.')

def menorValor(valores): 
    posicaoMenorValor = valores[0]

    for val in valores: 
        if val < posicaoMenorValor: 
            posicaoMenorValor = val
    return posicaoMenorValor

print(f'O menor valor inserido foi: {menorValor(valores)}.')

for a, b in enumerate(valores): 
    print(f'Na posição {a}, foi encontrado o valor {b}.')