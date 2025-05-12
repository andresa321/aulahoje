nomes = []

for i in range(5):
    nome = input("digite o nome: ")
    nomes.append(nome)

for nome in nomes:
    if nome[0] == "a" or nome[0] == "A":
        print(nome, end=" ")