nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
resultado = "" # Resultado é uma string vazia

if media >= 7:
    resultado = "Parabéns você passou por média"
elif media < 7 and media >= 4:
    resultado = "Você fará a final"
else:
    resultado = "Infelizmente você reprovou :("

print(resultado)



