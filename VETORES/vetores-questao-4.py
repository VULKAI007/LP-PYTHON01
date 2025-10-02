import os
os.system("cls")

pedido = []
v_pagar = []
lista_nomes = []
cardapio = {"PICANHA": 25.00, "LASANHA": 20.00, "STROGONOFF": 18.00, "BIFE ACEBOLA": 15.00, "PÃO COM OVO": 5.00}

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
    opcao = int(input("INSIRA O CÓGIDO DO PRATO DESEJADO: "))


    pedido.append(opcao)

    match opcao:
        case 1:
            lista_nomes.append("PICANHA")
            v_pagar.append(25)
        case 2:
            lista_nomes.append("LASANHA")
            v_pagar.append(20)
        case 3:
            lista_nomes.append("STROGONOFF")
            v_pagar.append(18)
        case 4:
            lista_nomes.append("BIFE ACEBOLADO")
            v_pagar.append(15)
        case 5:
            lista_nomes.append("PÃO COM OVOS")
            v_pagar.append(5)
        case _:
            print("INFOMR UM PRODUTO VÁLIDO")
    mais_pedidos = input("DESEJA REALIZAR MAIS ALGUM PEDIDO? (S/N) ").upper()

    if mais_pedidos == "N":
        break
    elif mais_pedidos != "N" and mais_pedidos != "S":
        print("POR FAVOR DIGITE UMA OPÇÃO VÁLIDA!")
    

if not v_pagar:
    print("NENHUM PEDIDO FEITO!")
else:
    for pedidos in pedido:
        print(f"==== LISTA DE PEDIDOS =====")
        print(f"PEDIDO: {lista_nomes} {v_pagar}")
    
    print("====== NOTA FISCAL ======")
    print(f"VALOR TOTAL A PAGAR {sum(v_pagar):.2f}")