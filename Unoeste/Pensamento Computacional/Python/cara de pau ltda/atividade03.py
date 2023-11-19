
# contadores
total_entrevistados = 0
homens_nao = 0
homens_sim = 0
respostas_sim = 0
respostas_nao = 0
mulheres_sim = 0
mulheres_nao = 0
indiferente = 0

# "While True" é utilizado para estruturas de repetições infinitas
while True:
    # Seção responsável pela entrada de dados dos entrevistados
    genero = input("Informe o genero (M/F): ").upper()
    idade = int(input("Digite suaa idade: "))
    resposta = input("Está gostando do nosso novo produto (S/N/I)? ").upper()

    # Aqui, erá efetuada a contagem dos entrevistados e atulizará seu contador
    total_entrevistados += 1

    # Abaixo está a relação de contagem da resposta "S" para cada genero seguido da
    # atualização do contador
    if resposta == 'S':
        respostas_sim += 1
        if genero == 'F':
            mulheres_sim += 1
            if genero == 'M':
                homens_sim += 1

    # Abaixo está a relação de contagem da resposta "S" para cada genero seguido da
    # atualização do contador
    elif resposta == 'N':
        respostas_nao += 1
        if genero == 'F':
            mulheres_nao += 1
            if genero == 'M':
                homens_nao += 1

    else:
        indiferente += 1

    # Nesta etapa, será identificado se a looping segue ou para.
    continuar_entrevista = input(
        "Deseja continuar a entrevista? (S/N): ").upper()
    if continuar_entrevista != 'S':
        break

# Impressão dos resultadosresultados
print("O número total de entrevistados, foi:", total_entrevistados)
print("O número total de pessoas que disseram sim, foi:", respostas_sim)
print("O número total de pessoas que disseram não, foi:", respostas_nao)
print("O número total de mulheres que disseram sim, foi:", mulheres_sim)
print("O número total de mulheres que disseram não, foi:", mulheres_nao)
print("O número total de homens que disseram nã, foi:", homens_nao)
print("O número total de homens que disseram sim, foi:", homens_sim)
print("O número total de respostas indiferente, foi:", indiferente)
