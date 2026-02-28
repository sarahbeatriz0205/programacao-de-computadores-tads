class Criptografia:
    def __init__(self):
        pass

    def dict_ascii(self):
        codigo_ascii = {}
        for i in range(0, 128):
            caractere = chr(i)
            codigo_ascii[caractere] = i
        return codigo_ascii
        
    def primeira_passada(self, frase):
        # Primeira passada
        frase_concat = []
        for caractere in frase:
            if caractere in self.dict_ascii():
                valor_caractere_tres = self.dict_ascii()[caractere] + 3
                chave_valor_tres = chr(valor_caractere_tres)
                frase = chave_valor_tres
                frase_concat.append(frase)
        frase_primeira_passada = "".join(frase_concat)
        return frase_primeira_passada

    def segunda_passada(self, frase):
        # Segunda passada
        frase_invertida = self.primeira_passada(frase)[::-1]
        frase = "".join(frase_invertida)
        return frase

    def passada_final(self, frase):
        # Terceira passada
        frase_list = []
        meio = len(self.segunda_passada(frase))//2
        lista = list(self.segunda_passada(frase))
        frase_div= lista[meio:]
        for caractere in frase_div:
            if caractere in self.dict_ascii():
                valor_retroceder_um = self.dict_ascii()[caractere] - 1 
                chave_valor_um = chr(valor_retroceder_um)
                frase_list.append(chave_valor_um)
        frase_passada_final = "".join(frase_list)
        frase_um = frase_div[:meio]
        frase_um_concat = "".join(frase_um)
        frase_cript = frase_um_concat + frase_passada_final
        return frase_cript

c = Criptografia()
frase = input("Frase: ")
print(c.passada_final(frase))