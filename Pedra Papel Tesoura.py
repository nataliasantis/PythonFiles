import random

entrada = int(input("Escolha:Pedra 1, Papel, 2, Tesoura 3:  "))


lista = ["pedra", "papel", "tesoura"]
usuario = lista[entrada-1]
computador = random.choice(lista)
print(usuario)
print(computador)

if usuario == computador:
    print("Empate!")
elif (usuario=="pedra") and (computador=="tesoura"):
    print("Você venceu!")
elif (usuario=="tesoura") and (computador=="pedra"):
    print("Você perdeu!")
elif (usuario=="tesoura") and (computador=="papel"):
    print("Você venceu!")
elif (usuario=="papel") and (computador=="tesoura"):
    print("Você perdeu!")
elif(usuario=="papel") and (computador == "pedra"):
    print("Você venceu!")
else:
    print("Você perdeu!")
#Regras
#Pedra ganha de tesoura
#Tesoura ganha de papel
#Papel ganha de pedra
