
vogais = ['a', 'e', 'i', 'o', 'u']


cont_consoantes = 0


consoantes = []


for i in range(10):
    caractere = input("Digite um caractere: ")
    if caractere.isalpha() and caractere.lower() not in vogais:
        cont_consoantes += 1
        consoantes.append(caractere)


print(f"Foram lidas {cont_consoantes} consoantes: {', '.join(consoantes)}")