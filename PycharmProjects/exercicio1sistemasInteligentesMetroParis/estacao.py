class Estacao:
    def __init__(self, num, corLinha):
        self.num = num
        self.corLinha = corLinha
        self.anterior = None # uma instância de estação, será o nó que gerou o nó atual


    def getNum(self):
        return self.num

    def getCorLinha(self):
        return self.corLinha