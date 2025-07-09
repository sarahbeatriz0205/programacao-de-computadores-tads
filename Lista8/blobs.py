num_casos = int(input())
comida_em_kg = []
dias = []

for i in range(0, num_casos): 
    comida_em_kg.append(float(input()))  

for i in range(0, num_casos):
    contador_dias = 0
    if comida_em_kg[i] <= 1.0: 
        dias.append(0)
    else: 
        while comida_em_kg[i] > 1.0:
            comida_em_kg[i] = comida_em_kg[i] / 2
            contador_dias += 1
        dias.append(contador_dias)

for dia in dias:
    print(dia, "dias")