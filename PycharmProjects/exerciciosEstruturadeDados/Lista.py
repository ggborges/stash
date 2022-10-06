from node import Node

class Lista:
    def __init__(self):
        self.head = None
        self._size = 0


    def _getNode(self, index):
        pointer = self.head
        for i in range(index - 1):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer



    def append(self, newNode):
        if self.head: # se o head não for nulo, adicionamos nos proximos
            # inserção quando a lista já possui 1 ou mais elementos
            pointer = self.head
            while(pointer.next): # se o nó seguinte não for nulo, passamos para o proximo
                pointer = pointer.next
            pointer.next = Node(newNode)
        else: # se o head for nulo, adicionamos o nó na cabeça da lista
            #primeira inserção
            self.head = Node(newNode)
        self._size = self._size + 1


    def __len__(self):
       """Retorna o tamanho da Lista"""
       return self._size


    def get(self, index):
        # a = lista[i] --- armazenamos o valor retornado por lista[i] na variavel a
        pointer = self._getNode(index)
        if pointer:
            # se o pointer não for nulo, retorna o valor do nó
            return pointer.data
        else:
            raise IndexError("list index out of range")


    def __getitem__(self, index):
        # a = lista[i] --- armazenamos o valor retornado por lista[i] na variavel a
        pointer = self._getNode(index)
        if pointer:
            # se o pointer não for nulo, retorna o valor do nó
            return pointer.data
        else:
            raise IndexError("list index out of range")

    def set(self, index, newNode):
        # lista[i] = x --- mudamos o elemendo i por x
        pointer = self._getNode(index)
        if pointer:
            pointer.data = newNode
        else:
            raise IndexError("list index out of range")


    def __setitem__(self, index, newNode):
        # lista[i] = x --- mudamos o elemendo i por x
        pointer = self._getNode(index)
        if pointer:
            pointer.data = newNode
        else:
            raise IndexError("list index out of range")


    def index(self, node):
        """Retorna o índice do nó na lista"""
        pointer = self.head
        index = 0;
        while(pointer): # enquanto o head não é nulo
            if pointer.data == node: # se o nó recebido for igual ao nó do pointer
                return index
            pointer = pointer.next
            index = index + 1
        raise ValueError('{} is not in list'.format(node))


    def insert(self, index, newNode):
        node = Node(newNode)
        if index == 0: # adicionar novo nó no começo (head) da lista
            node.next = self.head
            self.head = node
        else:
            pointer = self._getNode(index - 1)
            node.next = pointer.next
            pointer.next = node
        self._size = self._size + 1





lista1 = Lista()
print(len(lista1))
lista1.append(7)
print('Usando função len e lista1[]', len(lista1), lista1[0])
print('Usando função len e lista.get', len(lista1), lista1.get(0))
lista1.append(8)
print('Usando função len e lista1[]', len(lista1), lista1[1])
print('Usando função len e lista.get', len(lista1), lista1.get(1))
lista1.append(9)
print('Usando função len e lista1[]', len(lista1), lista1[2])
print('Usando função len e lista1.get', len(lista1), lista1.get(2))
print('index para o nó 8:', lista1.index(8))
print('index para o nó 9:', lista1.index(9))
print('index para o nó 7:', lista1.index(7))
print('index para o nó 10:', lista1.index(10))
