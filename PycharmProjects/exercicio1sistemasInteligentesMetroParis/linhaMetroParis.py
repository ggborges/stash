class MetroParis:
    def __init__(self, estacao_i, estacao_f):
        self.estadoInicial = estacao_i
        self.estadoFinal = estacao_f
        self.headLine = None # a cabeça da árvore, o nó (estacao) que começamos a busca para montarmos a árvore


    def getEstado_i(self):
        return self.estadoInicial


    def getEstado_f(self):
        return self.estadoFinal


    def getHeadLine(self):
        return self.headLine


