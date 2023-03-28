# Lendo os vetores de entrada
vetor1 = []
vetor2 = []

print("Digite os elementos do primeiro vetor:")
for i in range(5):
    elemento = int(input())
    vetor1.append(elemento)

print("Digite os elementos do segundo vetor:")
for i in range(5):
    elemento = int(input())
    vetor2.append(elemento)

# Gerando o terceiro vetor com os elementos intercalados
vetor3 = []
for i in range(5):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

# Exibindo o terceiro vetor gerado
print("O terceiro vetor gerado é:", vetor3)
