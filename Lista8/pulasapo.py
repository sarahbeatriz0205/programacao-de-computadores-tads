pulo_sapo, num_canos = map(int, input().split())
altura_canos = list(map(int, input().split()))
diferenca = 0
mensagem = "YOU WIN"

for i in range(1, num_canos):
    diferenca = abs(altura_canos[i] - altura_canos[i-1]) #não pode ter valor negativo
    if diferenca > pulo_sapo:
        mensagem = "GAME OVER"
        break
print(mensagem)