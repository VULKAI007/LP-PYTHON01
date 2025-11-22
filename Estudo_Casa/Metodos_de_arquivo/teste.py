import os
import time

# ERRO 1: Era os.sytem (digitação)
os.system('cls') 

lista_numero = []

while True:
    print("\n=========================================")
    print("(C) PARA CADASTRAR UM NÚMERO")
    print("(S) PARA FINALIZAR O PROGRAMA")
    print("(E) PARA EXIBIR OS NÚMEROS CADASTRADOS")
    print("==========================================")
    

    o = input("OPÇÃO: ").upper() 

    match o:
        case "C":
            print("\nDIGITE UM NÚMERO DE 0 A 10:")
            try:
                
                n = int(input("R: ")) 

                if n >= 0 and n <= 10:
                    lista_numero.append(n)
                    print("NÚMERO CADASTRADO!")
                elif n > 10 or n < 0:
                    print("POR FAVOR DIGITE UM NÚMERO VÁLIDO... SEU BURRO...")
            except ValueError:
                
                print("EU DISSE UM NÚMERO, NÃO UMA LETRA!")
            
            time.sleep(1) 

        case "E":

            if len(lista_numero) == 0:
                print("LISTA VAZIA....")
            else:
                print("\n--- NÚMEROS ---")
    
                for numero in lista_numero:
                    print(f"-> {numero}")
            
            input("\nPressione Enter para voltar...") 

        case "S":
            print("FINALIZANDO O PROGRAMA....")
            time.sleep(0.5)
            break
            
        case _: 
            print("OPÇÃO INVÁLIDA!")



    



