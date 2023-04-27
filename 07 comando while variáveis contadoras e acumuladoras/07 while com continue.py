# exemplo de while com continue
cont = 1 
while cont <= 10:
    cont += 1
    if (cont % 2 == 1):
        continue
    print(cont)