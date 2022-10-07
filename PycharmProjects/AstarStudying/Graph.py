import pandas as pd
from Vertice import Vertice
from listsqueuesandstacks import PriorityQueue
import math


class Graph:

    def __init__(self):

        self.list_of_nodes = []

        # Tabelas a serem consultadas
            # Tabela referente à função heurística h(n)
        # pathReta = ".\src\Distancia_em_linha_reta.xlsx"
        self.distancias_entre_nodes = pd.read_excel(".\src\Distancia_em_linha_reta.xlsx")

            # Tabela referente a função de caminho g(n)
        # pathReal = ".\src\Distancia_real.xlsx"
        self.distancias_reais = pd.read_excel(".\src\Distancia_real.xlsx")

    """def import_table_dist_h(self, path):
        self.distancias_entre_nodes = pd.read_excel(path)
        return True

    def import_table_dist_g(self, path):
        self.distancias_reais = pd.read_excel(path)
        return True"""

    def create_nodes(self):
        e1b = Vertice('E1', 'blue', 0)
        e2b = Vertice('E2', 'blue', 1)
        e2y = Vertice('E2', 'yellow', 1)
        e3b = Vertice('E3', 'blue', 2)
        e3r = Vertice('E3', 'red', 2)
        e4b = Vertice('E4', 'blue', 3)
        e4g = Vertice('E4', 'green', 3)
        e5b = Vertice('E5', 'blue', 4)
        e5y = Vertice('E5', 'yellow', 4)
        e6b = Vertice('E6', 'blue', 5)
        e7y = Vertice('E7', 'yellow', 6)
        e8y = Vertice('E8', 'yellow', 7)
        e8g = Vertice('E8', 'green', 7)
        e9y = Vertice('E9', 'yellow', 8)
        e9r = Vertice('E9', 'red', 8)
        e10y = Vertice('E10', 'yellow', 9)
        e11r = Vertice('E11', 'red', 10)
        e12g = Vertice('E12', 'green', 11)
        e13g = Vertice('E13', 'green', 12)
        e13r = Vertice('E13', 'red', 12)
        e14g = Vertice('E14', 'green', 13)

        e1b.add_adjacency_nodes(e2b)

        e2b.add_adjacency_nodes(e2y)
        e2b.add_adjacency_nodes(e1b)
        e2b.add_adjacency_nodes(e3b)

        e2y.add_adjacency_nodes(e2b)
        e2y.add_adjacency_nodes(e9y)
        e2y.add_adjacency_nodes(e10y)

        e3b.add_adjacency_nodes(e3r)
        e3b.add_adjacency_nodes(e2b)
        e3b.add_adjacency_nodes(e4b)

        e3r.add_adjacency_nodes(e3b)
        e3r.add_adjacency_nodes(e9r)
        e3r.add_adjacency_nodes(e13r)

        e4g.add_adjacency_nodes(e4b)
        e4g.add_adjacency_nodes(e13g)
        e4g.add_adjacency_nodes(e8g)

        e4b.add_adjacency_nodes(e4g)
        e4b.add_adjacency_nodes(e3b)
        e4b.add_adjacency_nodes(e5b)

        e5y.add_adjacency_nodes(e5b)
        e5y.add_adjacency_nodes(e7y)
        e5y.add_adjacency_nodes(e8y)

        e5b.add_adjacency_nodes(e5y)
        e5b.add_adjacency_nodes(e6b)
        e5b.add_adjacency_nodes(e4b)

        e6b.add_adjacency_nodes(e5b)

        e7y.add_adjacency_nodes(e5y)

        e8y.add_adjacency_nodes(e8g)
        e8y.add_adjacency_nodes(e5y)
        e8y.add_adjacency_nodes(e9y)

        e8g.add_adjacency_nodes(e8y)
        e8g.add_adjacency_nodes(e12g)
        e8g.add_adjacency_nodes(e4g)

        e9y.add_adjacency_nodes(e9r)
        e9y.add_adjacency_nodes(e8y)
        e9y.add_adjacency_nodes(e2y)

        e9r.add_adjacency_nodes(e9y)
        e9r.add_adjacency_nodes(e11r)
        e9r.add_adjacency_nodes(e3r)

        e10y.add_adjacency_nodes(e2y)

        e11r.add_adjacency_nodes(e9r)

        e12g.add_adjacency_nodes(e8g)

        e13g.add_adjacency_nodes(e13r)
        e13g.add_adjacency_nodes(e4g)
        e13g.add_adjacency_nodes(e14g)

        e13r.add_adjacency_nodes(e13g)
        e13r.add_adjacency_nodes(e3r)

        e14g.add_adjacency_nodes(e13g)

        self.list_of_nodes.append(e1b)
        self.list_of_nodes.append(e2b)
        self.list_of_nodes.append(e2y)
        self.list_of_nodes.append(e3b)
        self.list_of_nodes.append(e3r)
        self.list_of_nodes.append(e4b)
        self.list_of_nodes.append(e4g)
        self.list_of_nodes.append(e5b)
        self.list_of_nodes.append(e5y)
        self.list_of_nodes.append(e6b)
        self.list_of_nodes.append(e7y)
        self.list_of_nodes.append(e8y)
        self.list_of_nodes.append(e8g)
        self.list_of_nodes.append(e9r)
        self.list_of_nodes.append(e9y)
        self.list_of_nodes.append(e10y)
        self.list_of_nodes.append(e11r)
        self.list_of_nodes.append(e12g)
        self.list_of_nodes.append(e13g)
        self.list_of_nodes.append(e13r)
        self.list_of_nodes.append(e14g)

    def return_nodes(self):
        result = ''

        for nd in self.list_of_nodes:
            result = result + '(' + nd.estacao + ':' + nd.linha + '): ' + nd.print_adjacency_list() + '\n'

        return result

    def get_node(self, estacao: str, linha: str) -> Vertice:

        for nd in self.list_of_nodes:
            if nd.estacao == estacao and nd.linha == linha:
                print('Nó encontrado!')
                return nd
        print('Nó não encontrado!')


class Astar:

    def __init__(self):
        self.graph = None

        self.initial_state = None
        self.final_state = None

        #self.fronteira = PriorityQueue()  # Open Set
        self.fronteira = []

        self.visited_nodes = []
        self.found_solution = False
        self.solution = []

    def set_initial_and_final_states(self, initial_state: Vertice, final_state: Vertice):
        self.initial_state = initial_state
        self.final_state = final_state
        self.initial_state.func_f = self.func_h(self.initial_state)  # A função f do estado inicial é apenas a heurística
        self.fronteira.append(self.initial_state)

    def set_graph(self, graph: Graph):
        self.graph = graph

    def func_h(self, node):

        final_station = self.final_state.estacao
        final_line = self.final_state.linha
        a_station = node.estacao
        a_line = node.linha
        h = 0
        maior = ''

        if self.final_state.index >= node.index:
            maior = final_station
        else:
            maior = a_station

        table = self.graph.distancias_entre_nodes

        if self.final_state.index != node.index:
            for index, row in table.iterrows():

                not_null = True

                current_h = table.at[index, maior]

                # Verifico se a célula é um float
                # e então verifico se é nulo ('nan')
                if isinstance(current_h, float):
                    if math.isnan(current_h):
                        not_null = False

                # Verifico se a célula é uma string
                # e então verifico se é um hífen
                elif isinstance(current_h, str):
                    if current_h == '-':
                        # Mesma estação
                        not_null = False

                # Se a célula não for nula e corresponder ao nó que procuro
                # Então retorno o nó
                if not_null:
                    # print('h(n):' + str(index) + ' | ' + str(current_h) + ' | ' + str(row.get(maior, 0)))
                    if maior == a_station:  # Verificando a ordem
                        if index == self.final_state.index:
                            print('Achamos o h do adjacente atual (' + a_station +
                                  ' - ' + a_line + ') na tabela: ' + str(current_h))
                            h = (current_h / 30) * 60
                            print('(' + node.estacao + '|' + node.linha + ') -h(n) = ' + "{:.2f}".format(h) + 'min')
                    else:
                        if index == node.index:
                            print('Achamos o h do adjacente atual (' + a_station +
                                  ' - ' + a_line + ') na tabela: ' + str(current_h))
                            h = (current_h / 30) * 60
                            print('(' + node.estacao + '|' + node.linha + ') -h(n) = ' + "{:.2f}".format(h) + 'min')
                    # Retorna a variável 'current'
                    # Que corresponde à célula que guarda o valor da distância
                    # entre o estado 'test' e outro estado (index do vertice)

        node.func_h = h

        return h

    def func_g(self, node, adjacent):
        # O quanto que durou para chegar até o nó atual
        # node.previous.func_f + node.func_g
        g = 0

        node_station = node.estacao
        node_line = node.linha
        a_station = adjacent.estacao
        a_line = adjacent.linha

        maior = ''

        if node.index >= adjacent.index:
            maior = node_station
        else:
            maior = a_station

        table = self.graph.distancias_entre_nodes

        if node_station == a_station and node_line != a_line:  # Baldeação É PARA ESTAR NA FUNC_G
            print('Achamos o g do adjacente atual (' + a_station +
                  ' - ' + a_line + '): 4min [BALDEAÇÃO]')
            temp_g = 4
            g = temp_g + node.func_g
            print('(' + adjacent.estacao + '|' + adjacent.linha + ') -g(n) = ' + str(temp_g)
                  + 'min + ' + "{:.2f}".format(node.func_g) + 'min = ' + "{:.2f}".format(g) + 'min|')

        elif self.final_state.index != node.index:
            for index, row in table.iterrows():

                not_null = True

                current_g = table.at[index, maior]

                # Verifico se a célula é um float
                # e então verifico se é nulo ('nan')
                if isinstance(current_g, float):
                    if math.isnan(current_g):
                        not_null = False

                # Verifico se a célula é uma string
                # e então verifico se é um hífen
                elif isinstance(current_g, str):
                    if current_g == '-':
                        not_null = False

                # Se a célula não for nula e corresponder ao nó que procuro
                # Então retorno o nó
                if not_null:
                    # print('g(n):' + str(index) + ' | ' + str(current_g) + ' | ' + str(row.get(maior, 0)))
                    if maior == a_station:  # Verificando a ordem
                        if index == node.index:
                            print('Achamos o g do adjacente atual (' + a_station +
                                  ' - ' + a_line + ') com o seu pai (' + node_station +
                                  ' - ' + node_line + ') na tabela: ' + str(current_g))
                            temp_g = (current_g / 30) * 60
                            g = temp_g + node.func_g  # Adiciona ao g do pai

                            print('(' + adjacent.estacao + '|' + adjacent.linha + ') -g(n) = ' + "{:.2f}".format(temp_g)
                                  + 'min + ' + "{:.2f}".format(node.func_g) + 'min = ' + "{:.2f}".format(g) + 'min|')
                    else:
                        if index == adjacent.index:
                            print('Achamos o g do adjacente atual (' + a_station +
                                  ' - ' + a_line + ') na tabela: ' + str(current_g))
                            temp_g = (current_g / 30) * 60
                            g = temp_g + node.func_g  # Adiciona ao g do pai
                            print('(' + adjacent.estacao + '|' + adjacent.linha + ') -g(n) = ' + "{:.2f}".format(temp_g)
                                  + 'min + ' + "{:.2f}".format(node.func_g) + 'min = ' + "{:.2f}".format(g) + 'min|')

        return g

    @staticmethod
    def func_f(node):
        return node.func_f

    def print_solution(self):
        current = self.final_state
        solution = ''

        while current:
            station = '(' + current.estacao + '|' + current.linha + ')'
            if current is self.final_state:
                solution = station + '} :: Custo de caminho = ' + "{:.2f}".format(self.final_state.func_g) + 'min'
            elif current is self.initial_state:
                solution = 'Solução (caminho): {' + station + ' --> ' + solution
            else:
                solution = station + ' --> ' + solution

            current = current.previous

        return solution

    def print_closed_set(self):
        result = 'Estações visitadas: '
        if len(self.visited_nodes) > 0:
            index = 0
            for nd in self.visited_nodes:
                index += 1
                if len(self.visited_nodes) == 1:
                    result = result + '[(' + nd.estacao + '|' + nd.linha + ')]'
                elif index == 1:
                    result = result + '[(' + nd.estacao + '|' + nd.linha + ') ~ '
                elif nd is self.visited_nodes[len(self.visited_nodes)-1]:
                    result = result + '(' + nd.estacao + '|' + nd.linha + ')]'
                else:
                    result = result + '(' + nd.estacao + '|' + nd.linha + ') ~ '
        else:
            result = 'Nenhuma estação foi visitada.'

        return result

    def print_fronteira(self, iteri):
        result = ''
        front = self.fronteira
        tam = len(self.fronteira)

        index = 0
        for nd in front:

            if tam == 1:
                result = result + 'ITERAÇÃO `Nº' + str(iteri) + '´' + ' ..count: ' + str(tam) \
                         + '.. Fronteira: [' + nd.estacao + '|' + nd.linha + ']'

            elif index == 0:
                result = result + 'ITERAÇÃO `Nº' + str(iteri) + '´' + ' ..count: ' + str(tam) \
                         + '.. Fronteira: [(' + nd.estacao + '|' + nd.linha + '); '

            elif index == tam - 1:
                result = result + '(' + nd.estacao + '|' + nd.linha + ')]'

            else:
                result = result + '(' + nd.estacao + '|' + nd.linha + '); '


            index += 1

        print(result)


    def search(self):

        # ei = initial_state
        # ef = final_state

        current = None
        solution = []

        iteri = 0

        while len(self.fronteira) > 0 and not self.found_solution:
            # Enquanto a fronteira não estiver vazia e a solução não tiver sido encontrada
            iteri += 1
            print("\n")
            self.print_fronteira(iteri)
            #self.fronteira.print_queue(iteri)
            current = self.fronteira.pop(0)
            print("\n")
            print('POP: (' + current.estacao + '|' + current.linha + ')')
            print(current.print_adjacency_list() + "\n")
            print(self.print_closed_set() + "\n")
            self.visited_nodes.append(current)

            if current is self.final_state:  # Verificamos se chegamos ao objetivo
                solution.append(self.final_state)  # Adicionamos o nó à solução
                print('DONE')
                print(self.print_solution())
                self.found_solution = True
                return solution  # Retornamos a lista dos nós que compõem a solução (caminho)

            else:

                for nd in current.adjacency_list_of_nodes:
                    # Visitamos cada nó adjacente ao current e adicionamos à fronteira (openSet)
                    visited = False
                    for visited_node in self.visited_nodes:
                        # Testamos se o nó já foi visitado
                        if nd is visited_node:
                            print(' ---Estação já visitada! (' + nd.estacao + '|' + nd.linha + ')')
                            visited = True

                    if not visited:

                        temp_g = self.func_g(current, nd)

                        if nd in self.fronteira:  # Verificamos se o nó já estava na fronteira
                            print('Já estava na fronteira.')
                            if temp_g < nd.func_g:
                                nd.func_g = temp_g

                        else:
                            # Caso ele não esteja na fronteira
                            # adicionamos na fila, o primeiro é o nó mais aconselhável a explorar
                            nd.func_g = temp_g
                            nd.func_f = nd.func_g + self.func_h(nd)
                            nd.previous = current
                            self.fronteira.append(nd)
                            print('Inserting: [' + nd.estacao + '|' + nd.linha + '] -function f(n): '
                                + "{:.2f}".format(nd.func_f) + 'min [f(n) = h(n) + g(n)]')
                            self.fronteira.sort(key=lambda x: x.func_f)
                            print('Sorting....')

        if not self.found_solution:
            print('No solution.')
