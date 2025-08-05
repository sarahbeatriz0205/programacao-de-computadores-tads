n = int(input())
v = []
for i in range(n):
    v.append(int(input()))
resposta = 1
for i in range(n):
    n1 = v[i]
    for j in range(i+1, n):
        if v[i] == v[j]:
            continue
        n2 = v[j]
        cont = 2
        for k in range(j+1, n):
            if v[k] != n1:
                continue
            cont = cont + 1
            n1, n2 = n2, n1
        if cont > resposta: 
            resposta = cont
print(resposta)