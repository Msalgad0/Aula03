time1 = int (input("Digite o numero de gols do time 1: \n"))
time2 = int (input("Digite o numero de gols do time 2 \n"))

if time1 > time2 :
    print("Time 1 vencedor")
else:
    if time2 > time1:
        print("Time2 vencedor")
    else:
        print("Empate")