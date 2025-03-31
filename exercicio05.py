nota1 = float(input("Digite nota 1:\n"))
nota2 = float(input("Digite nota 2:\n"))
nota3 = float(input("Digite nota 3:\n"))

media = (nota1 + nota2 + nota3)/3
print(f"Sua média foi: {media}\n")
if media >= 7:
    print("Passou de ano!")
if media >=4  or media <=6:
    print("Recuperação!")
else:
    print("Reprovado!")