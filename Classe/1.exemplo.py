from dataclasses import dataclass

#ESTRUTURA DE DADOS: CALSSE.
@dataclass
class Pessoa:
    nome: str
    idade: int
    cpf: str

@dataclass
class Pet:
    nome: str
    idade: int
    peso: float

# EXEMPLO DE USO DE CLASSE
pessoa1 = Pessoa("ALICE", 30, "845.095.357-09")
pet1 = Pet("TOTÓ", 4, 5.5)

print("EXIBINDO DADOS DA PESSOA")
print(f"NOME: {pessoa1.nome}\nidade: {pessoa1.idade}\nCPF: {pessoa1.cpf}\n ")

print("EXIBINDO DADOS DO PET")
print(f"NOME: {pet1.nome}\nidade: {pet1.idade}\nPESO: {pet1.peso}")
