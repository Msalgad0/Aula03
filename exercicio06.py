time01 = input("Digite o nome do time 1: \n")
time02 = input("Digite o nome do time 2: \n")

novotime01 = int (input(f"Digite o numero de gols do {time01}: \n"))
novotime02 = int (input(f"Digite o numero de gols do {time02}: \n"))

if novotime01 > novotime02 :
    print(f"Time 1 {time01}")
else:
    if novotime02 > novotime01:
        print(f"Time {time02} vencedor")
    else:
        print("Empate")