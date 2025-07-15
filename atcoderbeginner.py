n_positivo = int(input())
numeros = [n_positivo]

while n_positivo != 1:
    if n_positivo % 2 == 0:
        n_positivo = n_positivo // 2
        numeros.append(n_positivo)
    else:
        n_positivo = (n_positivo * 3) + 1
        numeros.append(n_positivo)
print(*numeros)
