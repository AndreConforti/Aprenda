# # Uma loja tem tem uma política de descontos de acordo com o valor da compra do cliente.

# # Os descontos começam acima dos R$500
# # A cada 100 reais acima dos R$500,00 o cliente ganha 1\% de desconto cumulativo até 25\%. Por exemplo: R\$500 = 1\% || R$600,00 = 2\% ... etc...
# # Faça um programa que exiba essa tabela de descontos no seguinte formato:

# # Valordacompra - porcentagem de desconto - valor final

# valorDaCompra = float(input('Informe o valor da compra: R$ '))

# if valorDaCompra >= 500:
#     valorAcima = (valorDaCompra - 500) 
#     cumulativo = (valorAcima // 100) + 1
#     desconto = cumulativo / 100
#     if desconto > 0.25:
#         desconto = 0.25
#     valorFinal = valorDaCompra - (valorDaCompra * desconto)
# else:
#     desconto = 0
#     valorFinal = valorDaCompra


# print(f'''
# Valor da compra........: R$ {valorDaCompra:.2f}
# Porcentagem de desconto: {desconto:>10}
# Valor Final............: R$ {valorFinal:.2f}''')



valordacompra = 500

for i in range(1,26):
    print("valor da compra: ", valordacompra, "porcentagem de desconto:", i, "valor final", valordacompra *(1-(i/100)))
    valordacompra = valordacompra +100