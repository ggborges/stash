"""
    Classe vértice:
    - Representa 1 estado do problema
    - Cada estado representa 1 Estação em determinada linha (cor)
        - Exemplo:
                    Estação 9; linha vermelha - (e9, red)
                    Estação 9; linha amarela  - (e9, yellow)
        - Cada estação possui:
                    -   uma distância em linha reta para outra qualquer estação (função heurística)
                    -   a distância real para cada estação ( estado ) adjacente
                    -   lista de adjacência (lista de nós)
                            - Exemplo:
                                        (e9, red)
                                        func h:
                                            se for entre estações diferentes:
                                                acessa o doc para verificar distância em linha reta
                                                calcula em minutos
                                                    -   distância / velocidade = tempo
                                                        -   distancia dividida pela velocidade, enontramos o tempo
                                                tempo = dist/vel (km / 30)

                                            se não, é mudança de linha na mesma estação (baldeação):
                                                duração de 4 minutos
                                                tempo = 4 minutos

                                            retorna tempo

                                        func g:
                                            acessa o doc para verificar a distância real entre duas estações
                                            tempo = dist/vel (km / 30)

                                            retorna tempo

"""

class Vertice:

    def __init__(self, estacao, linha, index):
        self.estacao = estacao
        self.linha = linha
        self.index = index
        self.adjacency_list_of_nodes = []
        self.previous = None
        self.next = None
        self.func_h = 0
        self.func_g = 0
        self.func_f = 0
        # self.edges_list = []

    def add_adjacency_nodes(self, node):
        self.adjacency_list_of_nodes.append(node)

    def print_adjacency_list(self):
        result = 'adjacency_list: ['

        for node in self.adjacency_list_of_nodes:
            if node is self.adjacency_list_of_nodes[len(self.adjacency_list_of_nodes) - 1]:
                result = result + '(' +node.estacao + '|' + node.linha + ')'
            else:
                result = result + '(' + node.estacao + '|' + node.linha + ')' + ';'

        result = result + ']'
        return result

    def search_v(self, station, line):

        for nd in self.adjacency_list_of_nodes:
            if nd.estacao == station and nd.linha == line:
                return nd

