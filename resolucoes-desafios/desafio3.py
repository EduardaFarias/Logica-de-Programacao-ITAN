valor_venda = float(input("Informe o valor total de uma venda: "))


valor_desconto = valor_venda - (valor_venda * 0.10)
parcelas = valor_desconto / 3
comissao =  (valor_desconto * 0.05)


print(f"Valor com desconto de 10%: {valor_desconto:.2f}")
print(f"Valor de cada parcela")