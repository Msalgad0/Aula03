# Ler e mostrar nome,idade e salario.
nome = input ("Qual é seu nome\n")
idade = int(input("Quantos anos você tem?\n"))
salario = float(input("Quanto voce recebe por mês?\n"))
print(f"Prazer em conhecer você {nome}",
      f"Entao você tem {idade}",
      f"e já reccebe {salario:.2f} por mês\n")

aumento =float(input("Quanto foi a porcentagem de aumento?\n"))
aumentoReal = (salario * aumento) /100
novosalario = salario + aumentoReal
print (f"seu aumento foi {aumentoReal:.2f}\n")