import itertools
# Analise file.txt
# Linha 0 = numero de operacoes totais (nesse caso 4)
# A cada 3 linhas é uma unidade:
# A primeira linha fala o tipo de operação
# A segunda  e terceira são os valores para realizar a operação
i=0
j=0

file=f"./{int(input('Qual arquivo de teste deve ser usado? (1, 2 ou 3): '))}.txt"

lines=[]

def uniao(a,b):
    return a.union(b)

def inter(a,b):
    return a.intersection(b)

def dif(a,b):
    return a.difference(b)

def cart(a,b):
    return (list(itertools.product(a,b)))


num_lines = sum(1 for _ in open(file, "r"))

file = open(file, "r")

while i < num_lines:
    lines.append(file.readline().replace(',','').split())
    i+=1

num_op = lines[0]
lines.pop(0)

# for x in lines:
#     print(x)
          
#precisa converter as listas para sets, e dps fazer A.union(B)

# A = set(lines[0])
# B = set(lines[2])
# print(A.union(B))

# 3 em 3 checo o 0 e adiciona +2 no j
while j < num_lines-1:
    op = lines[j] #tipo de operacao (U,I,D,C)
    a = set(lines[j+1]) #conjunto A
    b = set(lines[j+2]) #conjunto B
    if op[0] == 'U':
        print(f'União do conjuto A {a} com o conjunto B {b}, resultado: {uniao(a,b)}')
    
    elif op[0] == 'I':
        print(f'Interseção do conjuto A {a} com o conjunto B {b}, resultado: {inter(a,b)}')
    
    elif op[0] == 'D':
        print(f'Diferença do conjuto A {a} com o conjunto B {b}, resultado: {dif(a,b)}')
    
    elif op[0] == 'C':
        print(f'Produto cartesiano do conjuto A {a} com o conjunto B {b}, resultado: {cart(a,b)}')
    print('='*130)

    j+=3 #itera pulando para as prox 3 linhas
