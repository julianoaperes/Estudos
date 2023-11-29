#Listas

#[] = list
#() = tupla
# linst = [a,b,c,d]
# positions: [0,1,2,3] 

num = [2,5,9,1]



#num[position2] = substituir por 3
num[2] = 3
print(num)

# .append = adiciona item na última posição
num.append(7)
print(num)

# .sort = organiza a lista em ordem
num.sort()
print(num)

# sort(reverse=True) = inverte a ordem da lista
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos.')

#.insert(a,n) = insere/acrescenta valores nas posições: a = posição e n = valor
# insere n na posição a.
num.insert(2, 0)
print(num)

# pop() sem nenhum parâmetro, elimina  o último item da lista
# os parâmtros inseridos refere-se a posções 
num.pop()
num.pop(3)
print(num)

#.remove = remove o item indicado 
num.remove(5)
print(num)


if 10 in num: 
    num.remove(10)
else:
    print('Não achei o número inserido')


