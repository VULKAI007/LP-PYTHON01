import os
os.system("cls")

print("======== NOTA DE PAGAMENTO ========")
valor = float(input("INFORME O VALOR: "))
op_pagamento = int(input("INFORME 1 PARA P.A VISTA, 2 PARA APRAZO: "))

match op_pagamento:
    case 1:
        valor2 = valor - valor*0.1
        print("============ NOTA =============")
        print(f"VALOR DO PRODUTO: {valor2}")
        print("FORMA DE PAGAMENTO: À VISTA")
        print(f"VALOR DO DESCONTO: {valor*0.1}")
        print(f"VALOR TOTAL A PAGAR: {valor2}")
    case 2:
        forma_pag = int(input("DIGITE EM QUANTAS VEZES DESEJA DIVIDIR(ATÉ 6X)"))
        lista_parcela = [1,2,3,4,5,6]

        if forma_pag in lista_parcela:
            print ("\n")
            print("============ NOTA =============")
            print(f"VALOR DO PRODUTO: {valor}")
            print(f"FORMA DE PAGAMENTO: À PRAZO")
            print(f"QUANTIDADE DE PARCELAS: {forma_pag}")
            print(f"VALOR POR PARCELAS: {valor / forma_pag}")
            print(f"TOTAL À PRAZO: {valor}")
        else:
            print("SÓ PODEMOS DIVIDIR EM ATÉ 6X")
    case _:
        print("DIGITE UMA OPÇÃO VÁLIDA!")