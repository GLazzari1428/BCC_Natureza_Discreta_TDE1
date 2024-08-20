# Analise file.txt
# Linha 0 = numero de operacoes totais (nesse caso 4)
# A cada 3 linhas é uma unidade:
# A primeira linha fala o tipo de operação
# A segunda  e terceira são os valores para realizar a operação
i=0

lines=[]

def id_op():
    pass

def uniao():
    pass

def inter():
    pass

def dife():
    pass

def cart():
    pass


num_lines = sum(1 for _ in open("ex1/file.txt", "r"))

file = open("ex1/file.txt", "r")

while i < num_lines:
    lines.append(file.readline().replace(',','').split())
    i+=1

print(lines)

#precisa converter as listas para sets, e dps fazer A.union(B)

A = set(lines[0])
B = set(lines[2])

print(A.union(B))