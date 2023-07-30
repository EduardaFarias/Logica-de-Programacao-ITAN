nome = input("Qual é o seu primeiro nome? ")
sobrenome = input("Qual é o seu primeiro sobrenome? ")
ano_nascimento = int(input("Qual foi o ano do seu nascimento? "))
ano_atual = int(input("Em qual ano estamos? "))
lugar  = input("De onde você é? ")
passatempo = input("O que você gosta de fazer no tempo livre? ")

idade = ano_atual - ano_nascimento

print(f"Meu nome é {nome} {sobrenome}, tenho {idade} anos, sou de {lugar} e gosto de {passatempo}.")
