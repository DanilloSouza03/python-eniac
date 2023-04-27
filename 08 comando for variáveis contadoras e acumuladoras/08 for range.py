#exemplo de for range
lista = [1,2,3,4,5,6,7,8,9,10]
nome = "Danillo"

for numero in range(6,10): #percorre números de 6 a 9
    print(numero)

print("------------------------------------")

for letra in nome: #percorre a string e printa cada letra
    print(letra)

print("------------------------------------")

for contagem in lista: #percorre a lista e mostra as mensagens de acordo
    if contagem >= 7:
        print("Maior ou igual a 7") #aqui ficam o 7, 8, 9, e 10
    elif contagem >= 4 and contagem <= 6:
        print("entre 4 a 6") #aqui ficam o 4, 5 e 6
    else:
        print("menor que 4") #aqui ficam o 1, 2 e 3