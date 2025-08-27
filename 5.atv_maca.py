import os
os.system('cls')

print("----- SELETOR DE MAÇA -----")
qtd = int(input("DIGITE A QUANTIDAE DE MAÇA QUE VC DESEJA: "))

if qtd >= 12:
    print("PARABÉNS! VOCÊ GANHOU UMA PROMOÇÃO, CADA MAÇA SAIRÁ PO 1 REAL")
    print("--- CARRINHO DE COMPRAS ---")
    valor = qtd * 1
    print("VALOR A SER PAGO: ", valor)
else:
    print("--- CARRINHOS DE COMPRAS ---")
    valor = qtd * 1.3
    print("VALOR A PAGAR: ", valor)