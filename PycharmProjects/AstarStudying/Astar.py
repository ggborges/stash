from listsqueuesandstacks import Queue, PriorityQueue

class Astar:

    def __init__(self, graph=None, ei=None, ef=None):

        self.graph = graph
        self.initial_state = ei
        self.final_state = ef
        self.fronteira = PriorityQueue() # Talvez eu precise implementar um fila com prioridades (priority queue)

    def search(self):

        ei = self.initial_state # Estado Inicial
        ef = self.final_state # Estado Final

        """
        for nd in graph.list_of_nodes
            if nd.estacao == ei.estacao and nd.linha == ei.linha
                
        
        """

        return

    def func_h(self):

        return

    def func_g(self):

        return

    def func_f(self):

        return