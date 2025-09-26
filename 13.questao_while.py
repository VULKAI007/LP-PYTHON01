import os
os.system("cls")

pedido = []
v_pagar = []

print("""
=========== MENU ====================
CÓDIGO       PRATO           VALOR
      
  1         PICANHA          R$25,00
  2         LASANHA          R$20,00
  3         STROGONOFF       R$18,00
  4         BIFE ACEBOLADO   R$15,00
  5         PÃO COM OVO      R$5,00
      
 (0)       PARA FINALIZAR O 
      
  """)

while True:
    opcao = int(input("INSIRA O CÓGIDO DO PRATOS DESEJADOS: "))

    if opcao == 0:
        break

    pedido.append(opcao)

    match opcao:
        case 1:
            v_pagar.append(25)
        case 2:
            v_pagar.append(20)
        case 3:
            v_pagar.append(18)
        case 4:
            v_pagar.append(15)
        case 5:
            v_pagar.append(5)
        case _:
            print("INFOMR UM PRODUTO VÁLIDO")
    

if not v_pagar:
    print("NENHUM PEDIDO FEITO!")
else:
    print("====== NOTA FISCAL ======")
    print(f"TOTAL DE ITENS PEDIDOS {len(pedido)}")
    print(f"VALOR TOTAL A PAGAR {sum(v_pagar):.2f}")