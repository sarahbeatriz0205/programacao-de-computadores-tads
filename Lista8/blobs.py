num_casos = int(input())
comida_em_kg = []
dias = []
contador_dias = 0

for i in range(0, num_casos):
    comida_em_kg.append(float(input()))
for i in range(0, num_casos):
    while (comida_em_kg[i] >= 1):
        comida_em_kg[i] = comida_em_kg[i] //2
        contador_dias += 1
    dias.append(contador_dias)
    contador_dias = 0

[print(dia, "dias") for dia in dias]