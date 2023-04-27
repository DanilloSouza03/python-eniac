# _*_ coding: utf-8 _*_
nome = input("Nome:")
altura = float(input("Altura(m):"))
massa = float(input("Massa(KG):")) 

imc = massa/(altura*altura)

print("Nome\tAltura\tMassa\tIMC\n{}\t{}\t{}\t{:.2f}".format(nome, altura, massa, imc))