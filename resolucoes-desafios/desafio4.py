nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a segunda nota: "))

media = ((nota1 + nota2 + nota3) / 3)
situacao = ""

if media >= 7:
    situacao = "foi aprovado :)"
elif media < 7 and media >= 4:
    situacao = "está na final :/"
    nova_nota = float(input("Digite a nota da final: "))
    if nova_nota >= 7:
        situacao = "foi aprovado :)"
else:
    situacao = "foi reprovado :("

print(f"Sua média é {media}, e você foi {situacao}")    