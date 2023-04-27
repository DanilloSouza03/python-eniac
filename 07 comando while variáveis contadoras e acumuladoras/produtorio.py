#-*-coding: utf-8-*-
n = int(input("Escreva o valor de N: "))

produtorio = 1 
i = 1 
while i <= n:
    produtorio = produtorio * i 
    i = i + 1
    
print("O produtorio de",n,"é",produtorio)    