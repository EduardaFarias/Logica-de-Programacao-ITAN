pocao = input("Digite o nome da poção: ")

tomouPocao = False
corPocao = ""

if(pocao == "Laxante Relaxante"):
    corPocao = "verde"

elif pocao == "Feitiço Sumiço":
    corPocao = "verde"

elif pocao == "Praga Amarga":
    corPocao = "Preto"

elif pocao == "Felizes para sempre":
    tomouPocao = True
    corPocao = "Azul"

else:
    tomouPocao = False
    corPocao = "Ele não bebeu essa poção"

if tomouPocao == True:
    print(f"O Shrek tomou a poção {pocao}, e a cor da poção era {corPocao}")
else:
    print(f"{corPocao}")