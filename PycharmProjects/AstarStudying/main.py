from Graph import Graph, Astar


def main():

    # Incializando o grafo com as estações
    # Depois inicializamos a busca A*
    graph = Graph()  # linha de paris
    graph.create_nodes()  # Cria os estados e suas respectivas listas de adjacencias

    # Escolhendo a estação inicial:
    num_i = input("Escolha o número (1 ~ 14) da estação inicial: ")
    try:
        number_i = int(num_i)
    except ValueError:
        print('Não digitou um número ou número invalido!')

    station_i = 'E' + str(number_i)
    print(f'Você escolheu a estação E{number_i}\n')
    print('cores: [ blue, yellow, red, green ]')
    line_i = input("Escolha a cor da estação inicial: ")
    print("\n")
    # Coletando o nó presente no grafo (caso ele exista)
    estado_inicial = graph.get_node(station_i, line_i)
    if estado_inicial:
        print('ESTAÇÃO INICIAL: [' + estado_inicial.estacao + '-' + estado_inicial.linha + ']\n')

    # Escolhendo a estação final
    num_f = input("Escolha o número (1 ~ 14) da estação final: ")
    try:
        number_f = int(num_f)
    except ValueError:
        print('Não digitou um número ou número invalido!')

    station_f = 'E' + str(number_f)
    print(f'Você escolheu a estação E{number_f}\n')
    print('cores: [ blue, yellow, red, green ]')
    line_f = input("Escolha a cor da estação final: ")
    print("\n")
    # Coletando o nó presente no grafo (caso ele exista)
    estado_final = graph.get_node(station_f, line_f)
    if estado_final:
        print('ESTAÇÃO FINAL: [' + estado_final.estacao + '-' + estado_final.linha + ']\n')

    # Inicializo nossa classe da busca
    a_star = Astar()
    # Associo o grafo ao algoritmo
    a_star.set_graph(graph)
    # Setamos os estados inicial e final
    a_star.set_initial_and_final_states(estado_inicial, estado_final)
    # Iniciamos a busca
    a_star.search()


if __name__ == '__main__':
    main()