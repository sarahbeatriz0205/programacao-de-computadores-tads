qtd_tamanhos = int(input()) #qtd de tamanhos existentes na loja
estoque = [] #estoque de chinelos
venda_efetivada = 0
for i in range(qtd_tamanhos):
    estoque.append(int(input()))

qtd_pedidos = int(input())
pedidos = []
for i in range(qtd_pedidos):
    pedidos.append(int(input()))

for i in range(qtd_pedidos):
    pedido = pedidos[i] - 1
    if estoque[pedido] != 0:
        venda_efetivada += 1
        estoque[pedido] = estoque[pedido] - 1

print(venda_efetivada)