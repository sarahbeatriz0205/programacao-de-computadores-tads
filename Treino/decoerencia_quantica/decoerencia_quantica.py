class Decoerencia_Quantica:
    def __init__(self, numero_qubits, qubits_estado_isolado, qubits_condicoes_normais):
        self.numero_qubits = numero_qubits
        self.qubits_estado_isolado = qubits_estado_isolado
        self.qubits_condicoes_normais = qubits_condicoes_normais
    
    def retorna_qubits_total(self): # retorna todos os qubits juntos em uma lista de strings
        qubits_totais = []
        for i in self.qubits_estado_isolado:
            for s in i:
                qubits_totais.append(s)
        for j in self.qubits_condicoes_normais:
            for n in j:
                qubits_totais.append(n)
        return qubits_totais
        
    def verifica_veracidade_qubits(self):
        numeros = {"0", "1", "*"}
        for q in self.retorna_qubits_total():
            if q not in numeros: # se q NÃO ESTIVER NO CONJUNTO, pq aí será inválido
                return False
        return True

    def taxa_decoerencia_quantica(self):
        contador_colapsados = 0
        contador_bits_superposicao = 0
        if self.verifica_veracidade_qubits():
            for superposicao_isolados in self.qubits_estado_isolado:
                for i in range(0, len(superposicao_isolados)):
                    for colapsados_cond_normais in self.qubits_condicoes_normais:
                        if superposicao_isolados[i] == "*" and colapsados_cond_normais[i] != "*":
                            contador_colapsados +=  1
            for superposicao  in self.qubits_estado_isolado:
                for s in superposicao:
                    if s == "*":
                        contador_bits_superposicao += 1
        taxa_decoerencia_quantica = contador_colapsados / contador_bits_superposicao
        return "Taxa de decoerência quântica: {:.2f}".format(taxa_decoerencia_quantica)

        
numero_qubits = int(input("Número de qubits: "))
qubits_estado_isolado = list(map(str, input("Qubits em estado isolado: ").split()))
qubits_condicoes_normais = list(map(str, input("Qubits em temperatura normal: ").split()))
d = Decoerencia_Quantica(numero_qubits, qubits_estado_isolado, qubits_condicoes_normais)
print("")
print(d.taxa_decoerencia_quantica())