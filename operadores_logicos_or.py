import os
os.system('cls')

nota = 10

#SE NOTA MENOR QUE ZERO OU MAIOR QUE 10.
if nota < 0 or nota > 10:
    print("NOTA INVÁLIDA.")
else:
    print(f"NOTA: {nota}")
