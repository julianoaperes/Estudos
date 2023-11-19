#Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.

n = (int(input('Digite um número inteiro: ')))
print('O sucessor do número é {} e' . format(n+1), end=' ')
print('seu antecessor é {}.' .format(n-1))