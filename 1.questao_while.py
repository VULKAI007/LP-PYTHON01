import os
os.system("cls")

while True:
    n1 = float(input("INFORME A NOTA DO ALUNO:"))
    if n1 >= 0 and n1 <= 10 :
        break
print(F" A NOTA É {n1}")