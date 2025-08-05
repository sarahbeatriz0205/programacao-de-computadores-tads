#essa merda, fiz um código bosta e deu erro
dna = input()
cont1 = dna.count("A")
cont2 = dna.count("T")
cont3 = dna.count("C")
cont4 = dna.count("G")

maior = cont1
if cont2 >= maior:
    maior = cont2
if cont3 >= maior:
    maior = cont3
if cont4 >= maior:
    maior = cont4

print(maior)