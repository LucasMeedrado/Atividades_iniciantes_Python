idades = []
alturas = []

for i in range(5):
    print(f'Pessoa {i+1}:')
    idade = int(input('Digite a idade: '))
    altura = float(input('Digite a altura (em metros): '))
    idades.append(idade)
    alturas.append(altura)

print('Idades (em ordem inversa):')
for idade in reversed(idades):
    print(idade)

print('Alturas (em ordem inversa):')
for altura in reversed(alturas):
    print(altura)