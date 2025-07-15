itens = int(input())
tamanho_sacola = int(input())
tamanho_item = map(int, input().split())

for item in tamanho_item:
    if sum(tamanho_item) <= tamanho_sacola:
        print("Yes")
    else:
        print("No")
