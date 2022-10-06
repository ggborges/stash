from Node import Node
from listsqueuesandstacks import Queue


class BinaryTree:

    def __init__(self):
        self.root_node = None
        self.number_of_nodes = 0


    def find_min(self):
        current = self.root_node
        while current.left_child:
            current = current.left_child

        return current

    def find_max(self):
        current = self.root_node
        while current.right_child:
            current = current.right_child

        return current

    def insert(self, data):
        # Insertion of a node in a BST takes O(h), where h is the height of the tree
        node = Node(data)
        # Verifica-se se a árvore possui um 'Nó Raiz'
        # Se o 'Nó Raiz' for nulo (None), então adicionamos o novo nó
        # como raiz da nossa árvore
        if self.root_node is None:
            self.root_node = node
            self.number_of_nodes = self.number_of_nodes + 1
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                # Se o novo nó for menor do que o atual (começando pela raiz)
                if node.data < current.data:
                    # Então partimos para o filho a esquerda
                    current = current.left_child
                    # Caso o current não tenha filho a esquerda
                    # Então adicionamos o nó ali
                    if current is None:
                        # Alteramos o filho à esquerda do pai
                        parent.left_child = node
                        self.number_of_nodes = self.number_of_nodes + 1
                        return
                    # Caso o novo nó for maior do que o atual (começando pela raiz)
                else:
                    # Partimos para o filho à direita
                    current = current.right_child
                    # Caso o current não tenha filho a esquerda
                    # Então adicionamos o nó ali
                    if current is None:
                        # Alteramos o filho à direita do pai
                        parent.right_child = node
                        return

    def get_node_with_parent(self, data):
        parent = None
        current = self.root_node
        if current is None:
            return (parent, None)
        while True:
            if current.data == data:
                return (parent, current)

            elif data < current.data:
                parent = current
                current = current.left_child

            elif data > current.data:
                parent = current
                current = current.right_child

        return (parent, current)

    def remove_using_search(self, data):
        # The remove operation takes O(h), where h is the height of the tree.

        parent, node = self.get_node_with_parent(data)

        if parent is None and node is None:
            return False

        # Get children count
        children_count = 0

        if node.get_left_child() and node.get_right_child():
            children_count = 2
        elif (node.left_child is None) and (node.right_child is None):
            children_count = 0
        else:
            children_count = 1

        # Se não tiver filhos
        if children_count == 0:
            # Testamos se é o root_node
            # se não tiver pai, é porque é a raiz da árvore
            if parent:
                # Testamos se é o filho a direita
                if parent.right_child is node:
                    # Então tiramos o node da árvore
                    parent.right_child = None
                # se não é o filho a direita, então é o left_child
                else:
                    # Tiramos o node da árvore
                    parent.left_child = None

        # Se tiver 1 filho
        elif children_count == 1:
            next_node = None
            # Testamos se o left_child existe
            if node.left_child:
                # Então atribuímos o filho à variável 'next_node'
                next_node = node.left_child
            # Se não, é o right_child
            else:
                # Atribuímos o filho à variável 'next_node'
                next_node = node.right_child

            # Testamos se é o root_node
            # se não tiver pai, é porque é a raiz da árvore (com apenas 1 filho)
            if parent:
                # Após guardarmos o valor do filho do nó a ser deletado
                # na variável 'next_node'
                # vamos associar o pai do nó excluído
                # ao filho do nó excluído ('next_node')

                # Testamos se o nó excluído era o filho à esquerda do pai
                if parent.left_child is node:
                    # Associamos o filho ('next_node') do nó excluído ('node')
                    # ao pai ('parent')
                    parent.left_child = next_node

                else:
                    # Atribuímos o filho ('next_node') do nó excluído ('node')
                    # ao pai ('parent')
                    parent.right_child = next_node

            # Se não existir um pai ('parent is None')
            # Então o nó a ser excluído ('node') é a raiz da árvore ('root_node')
            else:
                # Então o único filho da raiz, torna-se a própria raiz
                self.root_node = next_node

        # Caso tenha 2 filhos ('children_count == 2')
        else:
            parent_of_the_leftmost_node = node
            # Vamos descobrir qual o próximo nó mais próximo, porém maior, do que o 'node'
            leftmost_node = node.right_child
            # Enquanto houver filho à esquerda do right_child do 'node'
            while leftmost_node.left_child:
                parent_of_the_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child

            # Ao chegar ao filho mais à esquerda
            # do right_child do 'node'
            # Trocamos o valor ('data') do 'node'
            node.data = leftmost_node.data

            if parent_of_the_leftmost_node.left_child == leftmost_node:
                parent_of_the_leftmost_node.left_child = leftmost_node.right_child
            else:
                parent_of_the_leftmost_node.right_child = leftmost_node.right_child

    def search(self, data):
        current = self.root_node
        while True:

            # Se chegarmos à uma folha (leaf node)
            # então o data não existe na árvore
            # e retornamos None
            if current is None:
                return None

            # Encontramos o valor na árvore?
            elif current.data is data:
                return current

            # Se o data for menor do que o current
            # passamos para o nó à esquerda
            elif data < current.data:
                current = current.left_child

            # Se o data for maior do que o current
            # passamos para o nó à direita
            else:
                current = current.right_child

    # Depth-first search

    def in_order(self, root_node):
        current = root_node
        if current is None:
            return
        self.in_order(current.left_child)
        print(current.data)
        self.in_order(current.right_child)

    def pre_order(self, root_node):
        # Exemplo  *
        #        /   \
        #       +     -
        #     4  5   5  3
        # retorna: * + 4 5 - 5 3

        current = root_node
        if current is None:
            return
        print(current.data)
        self.pre_order(current.left_child)
        self.pre_order(current.right_child)

    def post_order(self, root_node):
        # Exemplo  *
        #        /   \
        #       +     -
        #     4  5   5  3
        # retorna: 4 5 + 5 3 - *

        current = root_node
        if current is None:
            return
        self.post_order(current.left_child)
        self.post_order(current.right_child)

        print(current.data)

    # Breadth-first search

    def breadth_first_search(self):

        visited_nodes = []
        fronteira = Queue()
        fronteira.enqueue(self.root_node)

        iter = 0

        while fronteira.count > 0:
            iter += 1
            fronteira.print_queue(iter)
            node = fronteira.pop()
            visited_nodes.append(node.data)

            if node.left_child:
                fronteira.enqueue(node.left_child)

            if node.right_child:
                fronteira.enqueue(node.right_child)

        return visited_nodes