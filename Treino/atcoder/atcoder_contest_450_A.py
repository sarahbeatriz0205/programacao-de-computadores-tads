n = int(input())
item = n
concatenar = ""

for i in range(1, n+1):
    concatenar += f"{item},"
    item = item - 1

print(concatenar[:-1])