numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

maior_numero = numero1

if numero2 > maior_numero:
    maior_numero = numero2

if numero3 > maior_numero:
    maior_numero = numero3

print("O maior número é:", maior_numero)