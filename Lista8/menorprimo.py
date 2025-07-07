#menor número primo maior que o inserido
n = int(input()) 
proximo_n = n + 1 
fim = False

while fim == False:
    continuar = False
    if proximo_n <= 1:
        continuar = True
    elif proximo_n == 2:
        continuar = False
    else:    
        for i in range(2, proximo_n):
            if proximo_n % i == 0:
                continuar = True
                break
        
    if continuar == False:
        fim = True
    else:
        proximo_n += 1 # 7

print(proximo_n)