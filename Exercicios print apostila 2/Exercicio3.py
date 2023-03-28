nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

média = (nota1 + nota2) / 4

print(f"A média final é: ", média)

if média == 10:
    print("Aprovado com distinção")
elif média >=7:
    print("O aluno está aprovado: ")
else:
    print("Aprovado com reprovado")
