# Os caracteres dentro da mascara {} indicam:
# O = irá preencher os caracteres em branco;
# O ^ centralizará o input;
# O 20 indicará a quantidade de caracteres inseridos pelo código
# O : é sintaxe para o código.


nome = input('Qual seu nome? ')
print('Prazer em te conhecer, {:=^20}!' .format(nome))
