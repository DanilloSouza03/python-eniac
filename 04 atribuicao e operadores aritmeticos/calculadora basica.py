num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, *, /): ")

resultado = num1

if operador == "+":
    resultado += num2
elif operador == "-":
    resultado -= num2
elif operador == "*":
    resultado *= num2
elif operador == "/":
    resultado /= num2
else:
    print("Operador inválido")
print("Resultado:", resultado)