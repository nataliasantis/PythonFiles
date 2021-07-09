print("Russian Roulette")
nomes = input("Digite o nome das pessoas separando por vírgula: ")
lista_nomes = nomes.split(", ")


membroslista = len(lista_nomes)
print(membroslista)

import random
#sorteado = random.randint(0, (membroslista-1))
#print(f"Quem pagará a conta será {lista_nomes[sorteado]}")

sorteado = random.choice(lista_nomes)
print(f"Quem pagará a conta hoje será {sorteado}")