temp = (int(input("Digite a temperatura: ")))
if temp < 10:
    print("Clima gelado")
elif 11 <= temp <=20:
    print("Clima frio")
elif 21 <= temp <=25:
    print("Clima normal")
elif 26 <= temp <=35:
    print("Clima quente")
else:
    print("Clima muito quente")