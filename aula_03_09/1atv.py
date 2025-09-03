import os
os.system("cls")

print("""
=========== MENU ====================
CÓDIGO       PRATO           VALOR
      
  1         PICANHA          R$25,00
  2         LASANHA          R$20,00
  3         STROGONOFF       R$18,00
  4         BIFE ACEBOLADO   R$15,00
  5         PÃO COM OVO      R$5,00

  """)

opcao = int(input("DIGITE O CÓDIGO DO PRATO: "))


match opcao:
    case 1:
        nome = "PICANHA"
        valor = 25.0
    case 2:
        nome = "LASANHA"
        valor = 20.0
    case 3:
        nome= "STROGONOFF"
        valor = 18.0
    case 4:
        nome = "BIFE ACEBOLADO"
        valor = 15.0
    case 5:
        nome = "PÃO COM OVO"
        valor = 5.0
    case _:
        print("DIGITE UM VALOR VÁLIDO")

print(f"PRATO: {nome} \nVALOR: {valor}")