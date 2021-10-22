#Input é usado para fazer uma pergunta ao usuario, onde ele vai dar uma respota
#OBS: Para realisar conta tem que ser especificado numero INT ou FLOAT.

nome = input("Qual o nome do seu filho? ")
nota1 = float(input(f"Qual a primeira nota do {nome} ?"))
nota2 = float(input(f"Qual a segunda nota do {nome} ?"))
nota3 = float(input(f"Qual a terceira nota do {nome} ?"))

media = (nota1 + nota2 + nota3)/3

print(f"A média do {nome} é de {media}")