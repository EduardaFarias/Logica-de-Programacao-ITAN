num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação que deseja realizar: ")

resultado = 0 
## Resultado vai ser igual a 0 e não igual a "" porque aqui eu vou guardar um valor numérico e não uma frase como no exemplo do cálculo das médias

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2

print(resultado)
