class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def getValor(self):
        return self.valor

    def setEsquerda(self, esquerda):
        self.esquerda = esquerda

    def setDireita(self, direita):
        self.direita = direita

    def getEsquerda(self):
        return self.esquerda

    def getDireita(self):
        return self.direita



no1 = No(10)
no2 = No(20)
no3 = No(30)

no1.setEsquerda(no2)
no1.setDireita(no3)

print('Valor:', no1.getValor())
print('Esquerda:', no1.getEsquerda().getValor())
print('Direita:', no1.getDireita().getValor())