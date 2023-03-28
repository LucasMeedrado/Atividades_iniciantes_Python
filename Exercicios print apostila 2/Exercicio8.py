print("Responda sim ou não às perguntas abaixo:")
pergunta1 = input("Telefonou para a vítima? ")
pergunta2 = input("Esteve no local do crime? ")
pergunta3 = input("Mora perto da vítima? ")
pergunta4 = input("Devia para a vítima? ")
pergunta5 = input("Já trabalhou com a vítima? ")

respostas_positivas = 0

if pergunta1 == "sim":
    respostas_positivas += 1
if pergunta2 == "sim":
    respostas_positivas += 1
if pergunta3 == "sim":
    respostas_positivas += 1
if pergunta4 == "sim":
    respostas_positivas += 1
if pergunta5 == "sim":
    respostas_positivas += 1

if respostas_positivas == 2:
    print("Você é considerado um SUSPEITO do crime.")
elif respostas_positivas >= 3 and respostas_positivas <= 4:
    print("Você é considerado um CÚMPLICE do crime.")
elif respostas_positivas == 5:
    print("Você é considerado o ASSASSINO.")
else:
    print("Você é considerado INOCENTE.") 