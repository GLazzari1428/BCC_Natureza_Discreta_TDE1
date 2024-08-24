import itertools
# Analise file.txt
# Linha 0 = numero de operacoes totais (nesse caso 4)
# A cada 3 linhas é uma unidade:
# A primeira linha fala o tipo de operação
# A segunda  e terceira são os valores para realizar a operação

file = f"./1.txt" #variavel que seleciona o arquivo de teste 1.txt, 2.txt ou 3.txt

i = 0
j = 0
lines = []

def uniao(a, b):
    return a.union(b)

def inter(a, b):
    return a.intersection(b)

def dif(a, b):
    return a.difference(b)

def cart(a, b):
    return (list(itertools.product(a, b)))

num_lines = sum(1 for _ in open(file, "r"))

file = open(file, "r")

while i < num_lines:
    lines.append(file.readline().replace(',', '').split())
    i += 1

lines.pop(0)  #remove a primeira linha

while j < num_lines - 1:
    op = lines[j]  #tipo de operacao (U,I,D,C)
    a = set(lines[j + 1])  #conjunto A
    b = set(lines[j + 2])  #conjunto B
    if op[0] == 'U':
        print(f'União: conjunto 1 {a}, conjunto 2 {b}. Resultado: {uniao(a,b)}')
        
    elif op[0] == 'I':
        print(f'Interseção: conjunto 1 {a}, conjunto 2 {b}. Resultado: {inter(a,b)}')

    elif op[0] == 'D':
        print(f'Diferença: conjuto 1 {a}, conjunto 2 {b}. Resultado: {dif(a,b)}')

    elif op[0] == 'C':
        print(f'Produto cartesiano: conjuto 1 {a}, conjunto 2 {b}. Resultado: {cart(a,b)}')

    j += 3  #itera pulando para as prox 3 linhas