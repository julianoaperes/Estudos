
import random
sortnum = random.randint(0, 5)

print('O programa já escolheu o número. Agora adivinhe!')

choosenum = int(input("Escolha o número: "))
if sortnum == choosenum:
    print('Você acertou!')
else:
    print('Não foi dessa vez!')
