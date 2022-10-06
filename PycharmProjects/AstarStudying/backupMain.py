from Node import Node
from binarysearchtree import BinaryTree
from listsqueuesandstacks import *
import pandas as pd
from Graph import Graph, Astar
from Vertice import Vertice
import math

def array_to_tree(array, tree):
    count = 1
    for nd in array:

        if nd is array[array.__len__() - 1]:
            tree.insert(nd.data)
            print('Inserting on Tree: ' + str(nd.data) + ' (n' + str(count) + ').')
        else:
            tree.insert(nd.data)
            print('Inserting on Tree: ' + str(nd.data) + ' (n' + str(count) + '); ')

        count = count + 1

def array_to_LinkedList(array, list):
    count = 1
    for word in array:

        if word is array[len(array) - 1]:
            list.append(word)
            print('Inserting on List: "' + word + '".')
        else:
            list.append(word)
            print('Inserting on List: "' + word + '";')
            count = count + 1




def main():

    """
    n1 = Node(3)
    n2 = Node(2)
    n3 = Node(6)
    n4 = Node(13)
    n5 = Node(8)
    n6 = Node(1)
    n7 = Node(5)
    n8 = Node(15)
    n9 = Node(7)
    n10 = Node(11)

    my_array = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]
    array_words = ['egg', 'ham', 'spam', 'dani', 'canhao', 'pronto']

    bst = BinaryTree()
    words = SinglyLinkedList()

    # count = 1
    for nd in my_array:

        if nd is my_array[my_array.__len__() - 1]:
            bst.insert(nd.data)
            print('Inserting: ' + str(nd.data) + ' (n' + str(count) + ').')
        else:
            bst.insert(nd.data)
            print('Inserting: ' + str(nd.data) + ' (n' + str(count) + '); ')

    #   count = count + 1

    # Insertion on tree
    array_to_tree(my_array, bst)

    print('Máximo: ' + str(bst.find_max().data))
    print('Mínimo: ' + str(bst.find_min().data))
    print('Root node: ' + str(bst.root_node.data))
    print('In-order: ')
    print(bst.in_order(bst.root_node))
    print('Breadth-first Search:')

    visited = bst.breadth_first_search()

    for node in visited:
        print(str(node) + ';')

    print('Insertion on Singly Linked List:')
    array_to_LinkedList(array_words, words)
    words.print_list()
    """




    #tabela[linha, coluna]
    #tabela = pd.read_excel(r"D:\Users\gugab\Documents\Ciencias da Computação\Sistemas Inteligentes\Distancia_em_linha_reta.xlsx")

    #print(tabela)

    #tabela_dist_linha_reta = r"D:\Users\gugab\Documents\Ciencias da Computação\Sistemas Inteligentes\Distancia_em_linha_reta.xlsx"
    #tabela_dist_real = r"D:\Users\gugab\Documents\Ciencias da Computação\Sistemas Inteligentes\Distancia_real.xlsx"
    """
    e2y = Vertice('E2', 'yellow')
    e2b = Vertice('E2', 'blue')

    e1b = Vertice('E1', 'blue')
    e3b = Vertice('E3', 'blue')
    e10y = Vertice('E10', 'yellow')
    e9y = Vertice('E9', 'yellow')

    e2y.add_adjacency_nodes(e10y)
    e2y.add_adjacency_nodes(e9y)
    e2b.add_adjacency_nodes(e1b)
    e2b.add_adjacency_nodes(e3b)

    print(e2y.print_adjacency_list())
    print(e2b.print_adjacency_list())
    """

    # Incializando o grafo com as estações
    # Depois inicializamos a busca A*
    graph = Graph() # linha de paris
    graph.create_nodes() # Cria os estados e suas respectivas listas de adjacencias

    # Escolhendo a estação inicial:
    num_i = input("Escolha o número (1 ~ 14) da estação inicial: ")
    try:
        number_i = int(num_i)
    except ValueError:
        print('Não digitou um número ou número invalido!')

    station_i = 'E' + str(number_i)
    print(f'Você escolheu a estação E{number_i}')
    print('cores: [ blue, yellow, red, green ]')
    line_i = input("Escolha a cor da estação inicial: ")

    estado_inicial = graph.get_node(station_i, line_i)
    if estado_inicial:
        print(estado_inicial.estacao + ' - ' + estado_inicial.linha)

    # Escolhendo a estação final
    num_f = input("Escolha o número (1 ~ 14) da estação final: ")
    try:
        number_f = int(num_f)
    except ValueError:
        print('Não digitou um número ou número invalido!')

    station_f = 'E' + str(number_f)
    print(f'Você escolheu a estação E{number_f}')
    print('cores: [ blue, yellow, red, green ]')
    line_f = input("Escolha a cor da estação final: ")

    estado_final = graph.get_node(station_f, line_f)
    if estado_final:
        print(estado_final.estacao + ' - ' + estado_final.linha)

    a_star = Astar()
    a_star.set_graph(graph)
    a_star.set_initial_and_final_states(estado_inicial, estado_final)
    a_star.search()


    #print(graph.return_nodes())
    #print(graph.distancias_entre_nodes)
    #print(graph.distancias_reais)
    test = 'E7'

    #table1 = graph.distancias_entre_nodes
    #table2 = graph.distancias_reais
    #print(table1)
    #print(table2)

    """
    for index, row in table1.iterrows():

        not_null = True

        current = table1.at[index, test]

        # Verifico se a célula é um float
        # e então verifico se é nulo ('nan')
        if isinstance(current, float):
            if math.isnan(current):
                not_null = False

        # Verifico se a célula é uma string
        # e então verifico se é um hífen
        elif isinstance(current, str):
            if current == '-':
                not_null = False

        # Se a célula não for nula e corresponder ao nó que procuro
        # Então retorno o nó
        if not_null:
            print('h(n):' + str(index) + ' | ' + str(current) + ' | ' + str(row.get(test, 0)))
            # Retorna a variável 'current'
            # Que corresponde à célula que guarda o valor da distância
            # entre o estado 'test' e outro estado (index do vertice)

    for idx, r in table2.iterrows():

        not_null = True

        current = table2.at[idx, test]

        # Verifico se a célula é um float
        # e então verifico se é nulo ('nan')
        if isinstance(current, float):
            if math.isnan(current):
                not_null = False

        # Verifico se a célula é uma string
        # e então verifico se é um hífen
        elif isinstance(current, str):
            if current == '-':
                not_null = False

        # Se a célula não for nula e corresponder ao nó que procuro
        # Então retorno o nó
        if not_null:

            print('g(n):'+str(idx)+' | '+str(current)+' | '+str(r.get(test, 0)))
            # Retorna a variável 'current'
            # Que corresponde à célula que guarda o valor da distância
            # entre o estado 'test' e outro estado (index do vertice)
    """

    """fila = PriorityQueue()
    set_of_nodes = [10, 12, 8, 15, 6, 17, 14, 9, 11, 3, 4, 13, 2]
    iter = 0
    for i in set_of_nodes:
        iter += 1
        fila.enqueue(i)
        fila.print_queue(iter)"""

if __name__ == '__main__':
    main()
