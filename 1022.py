#algoritmo de Euclides
def mdc(n, m):
    anterior = n
    atual    = m
    resto    = anterior % atual

    while resto != 0:
        anterior = atual
        atual    = resto
        resto    = anterior % atual

    return atual

num_lines = int(input())

for i in range(num_lines):
    str = input()
    n1, div01, d1, oper, n2, div02, d2 = str.split(" ")
    n1 = int(n1)
    d1 = int(d1)
    n2 = int(n2)
    d2 = int(d2)
    
    if oper == "+":
        num = n1 * d2 + n2 * d1
        den = d1 * d2
    elif oper == '-':
        num = n1 * d2 - n2 * d1
        den = d1 * d2
    elif oper == '*':
        num = n1 * n2
        den = d1 * d2
    elif oper == '/':
        num = n1 * d2
        den = n2 * d1
    div = mdc(num, den)

    print("{}/{} = {}/{}".format(num, den, int(num/div), int(den/div)))