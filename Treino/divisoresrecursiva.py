def inverter(lista):
    print(lista)
    if lista == []: # lista vazia, retorna ela mesma
        return lista
    return lista[-1:] + inverter(lista[:-1])

lista = inverter([1, 2, 3, 4, 5])
print(lista) # [5, 4, 3, 2, 1]
