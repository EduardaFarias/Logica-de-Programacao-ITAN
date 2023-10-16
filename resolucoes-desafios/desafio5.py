x = int(input("Informe o valor de x: "))
y = int(input("Informe o valor de y: "))

resultado = 0

if x >= 0 and y >= 0:
    resultado = x + y
elif x >= 0 and y < 0:
    resultado = x + (y ** 2)
elif x < 0 and y >= 0:
    resultado = (x**2) + y
else:
    resultado = (x**2) + (y**2)

print(f"A função f({x}, {y}) é igual a {resultado}")
