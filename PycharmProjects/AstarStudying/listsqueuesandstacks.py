class NodeList:

    def __init__(self, data=None):
        self.numero = data
        self.next = None


class NodeListDoubly:

    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous


class SinglyLinkedList:

    def __init__(self):
        self.tail = None  # primeiro da lista
        self.head = None  # último da lista
        self.size = 0

    # Insert operation
    def append_amador(self, data):
        # Criamos o nó que armazena o valor de 'data'
        node = NodeList(data)

        # Se a fila estiver vazia (tail == None), então associamos node ao tail
        if self.tail == None:
            self.tail = node
        else:
            # Começamos a buscar pelo lugar vazio, iniciando pelo tail
            current = self.tail

            # Enquanto houver um próximo (enquanto não chegar ao fim da lista)
            while current.next:
                # Passamos para o próxima da lista
                current = current.next
            # Quando chegamos ao último nó da lista, adicionamos o novo nó ao next
            current.next = node

        self.size += 1

    def append(self, data):
        node = NodeList(data)

        # Se não existir um head, é pq a lista é vazia
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node

        self.size += 1

    def print_list(self):
        current = self.tail
        count = 0
        while current:

            if current.next is None:
                count = count + 1
                print(str(count) + 'º- ' + str(current.data) + '.')
                current = current.next

            else:
                count = count + 1
                print(str(count) + 'º- ' + str(current.data) + ';')
                current = current.next

    # Retorna data por data e não armazena os valores de val
    # yield só permite a leitura uma única vez
    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    # Usando um gerador ()
    def iter_all(self):
        current = self.tail
        result = ()
        while current:
            val = current.data
            current = current.next
            result.add(val)

        return result

    def delete_node(self, data):
        current = self.tail
        previous = self.tail
        while current:
            if current.data == data:
                if current == self.tail:  # Se for o primeiro nó da lista
                    self.tail = current.next  # Pegamos os próximo para ser o tail
                else:
                    previous.next = current.next
                self.size -= 1
                return

            previous = current
            current = current.next

    def search(self, data):
        for nd in self.iter():
            if data == nd:
                return True
        return False

    def clear(self):
        self.tail = None
        self.head = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None  # Primeiro da lista
        self.tail = None  # Último da lista
        self.count = 0

    def append(self, data):

        new_node = NodeListDoubly(data, None, None)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def delete_node(self, data):
        current = self.head
        node_deleted = False

        if current is None:  # Verificando se a lista está vazia
            node_deleted = False

        elif current.data == data:  # Verificando se vamos deletar o head
            self.head = current.next
            self.head.previous = None
            node_deleted = True

        elif self.tail.data == data:  # Verificando se vamos deletar o tail
            self.tail = self.tail.previous
            self.tail.next = None
            node_deleted = True

        # Se chegamos nesse ponto, então a fila não está vazia
        # O nó a ser excluído não é o head, nem o tail
        # Então é um nó entre dois nós
        else:
            while current:
                if current.data == data:
                    # Ligamos o próximo de seu anterior ao seu próximo
                    current.previous.next = current.next
                    # E o anterior do próximo ao seu anterior
                    current.next.previous = current.previous
                    node_deleted = True
                current = current.next

        if node_deleted:
            self.count -= 1

    """def get_node(self, node):
        current = self.head

        while current:
            if current.data.estacao == node.estacao and current.data.linha == node.linha:
"""


class StackList:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = NodeList(data)
        if self.top:  # Se a lista não estiver vazia
            node.next = self.top
            self.top = node

        else:  # Caso a lista esteja vazia
            self.top = node

        self.size += 1

    # Remove o topo da pilha
    def pop(self, data):
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:  # Verificando se temos apenas 1 nó na pilha
                self.top = self.top.next

            else:  # Chegamos aqui caso tenhamos apenas 1 nó na pilha
                self.top = None

            return data

        else:  # Chegamos aqui caso a pilha esteja vazia
            return None

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None


class ListQueue:
    def __init__(self):
        self.items = []
        self.size = 0


class StackQueue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []


class Queue:
    # Node-based queue
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        new_node = NodeListDoubly(data, None, None)
        # new_node = node

        if self.head is None:  # Se a lista estiver vazia
            self.head = new_node  # Adicionamos o nó como primeiro da fila
            self.tail = self.head  # Como só tem 1 nó, ele também é o último

        else:  # Se não estiver vazia
            new_node.previous = self.tail  # O último torna-se o anterior ao novo nó
            self.tail.next = new_node  # O novo nó torna-se o próximo do tail
            self.tail = new_node  # O novo nó agora é o último (tail) da fila

        self.count += 1

    def dequeue(self):
        # Como se fosse o método pop
        current = self.head

        if self.count == 1:  # Temos apenas um nó (sendo tanto o 'head' tanto o 'tail')
            self.count -= 1
            self.head = None
            self.tail = None

        elif self.count > 1:
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1

    def pop(self):
        current = self.head

        if self.count == 1:
            self.head = None
            self.tail = None
            self.count -= 1
            return current.data

        elif self.count > 1:
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1
            return current.data

    def print_queue(self, num):
        current = self.head
        result = ''

        while current:
            if current is self.head and current is self.tail:
                result = result + 'nº' + str(num) + ' [' + str(current.data.data) + ']'
                current = current.next
            elif current is self.head:
                result = result + 'nº' + str(num) + ' [' + str(current.data.data) + '; '
                current = current.next
            elif current is self.tail:
                result = result + str(current.data.data) + ']'
                current = current.next
            else:
                result = result + str(current.data.data) + '; '
                current = current.next

        print(result)


class PriorityQueue:

    # Node-based queue
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        new_node = NodeListDoubly(data, None, None)
        # new_node = node

        current = self.tail
        not_inserted = True

        if self.head is None:  # Se a lista estiver vazia
            self.head = new_node  # Adicionamos o nó como primeiro da fila
            self.tail = self.head  # Como só tem 1 nó, ele também é o último
            print('Inserting: [' + new_node.data.estacao + '|' + new_node.data.linha + '] -function f(n): '
                  + "{:.2f}".format(new_node.data.func_f) + 'min [f(n) = h(n) + g(n)]')

            not_inserted = False

        else:  # Se não estiver vazia
            while current and not_inserted:

                if data.func_f < current.data.func_f:
                    # Se nossa função é menor do que o atual, passamos pro de cima (anterior)
                    if current.previous is None and current is self.head:
                        self.head.previous = new_node
                        new_node.next = self.head
                        self.head = new_node
                        print('Inserting: [' + new_node.data.estacao + '|' + new_node.data.linha + '] -function f(n): '
                              + "{:.2f}".format(new_node.data.func_f) + 'min [f(n) = h(n) + g(n)]')

                        not_inserted = False
                    else:
                        current = current.previous
                        print('Looking... [' + new_node.data.estacao + '|' + new_node.data.linha +
                              '] -function f(n): ' + "{:.2f}".format(new_node.data.func_f) + 'min [f(n) = h(n) + g(n)]')

                elif current is self.tail:
                    new_node.previous = self.tail  # O último torna-se o anterior ao novo nó
                    self.tail.next = new_node  # O novo nó torna-se o próximo do tail
                    self.tail = new_node  # O novo nó agora é o último (tail) da fila
                    print('Inserting: [' + new_node.data.estacao + '|' + new_node.data.linha + '] -function f(n): ' +
                          "{:.2f}".format(new_node.data.func_f) + 'min [f(n) = h(n) + g(n)]')

                    not_inserted = False

                else:
                    new_node.previous = current
                    new_node.next = current.next
                    current.next = new_node
                    print('Inserting: [' + new_node.data.estacao + '|' + new_node.data.linha +
                          '] -function f(n): ' + "{:.2f}".format(new_node.data.func_f) + 'min [f(n) = h(n) + g(n)]')

                    not_inserted = False

        self.count += 1



    def dequeue(self):
        # Como se fosse o método pop
        current = self.head

        if self.count == 1:  # Temos apenas um nó (sendo tanto o 'head' tanto o 'tail')
            self.count -= 1
            self.head = None
            self.tail = None

        elif self.count > 1:
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1

    def pop(self):
        # Retorna o primeiro nó da fila

        current = self.head

        if self.count == 1:
            # Só tem uma estação na fronteira
            self.head = None
            self.tail = None


        elif self.count > 1:
            self.head = current.next
            self.head.previous = None

        self.count -= 1
        return current.data

    def print_queue(self, num):
        current = self.head
        result = ''

        while current:
            if current is self.head and current is self.tail:
                result = result + 'ITERAÇÃO `Nº' + str(num) + '´' + ' ..count: ' + str(self.count) \
                         + '.. Fronteira: [' + current.data.estacao + '|' + current.data.linha + ']'
                current = current.next
            elif current is self.head:
                result = result + 'ITERAÇÃO `Nº' + str(num) + '´' + ' ..count: ' + str(self.count) \
                         + '.. Fronteira: [(' + current.data.estacao + '|' + current.data.linha + '); '
                current = current.next
            elif current is self.tail:
                result = result + '(' + current.data.estacao + '|' + current.data.linha + ')]'
                current = current.next
            else:
                result = result + '(' + current.data.estacao + '|' + current.data.linha + '); '
                current = current.next

        print(result)

    def is_there(self, node):
        current = self.head

        founded = False

        while current:
            if current.data is node:
                founded = True
                return founded
            current = current.next

        return founded


if __name__ == '__main__':

    fila = PriorityQueue()
    set_of_nodes = [10, 12, 8, 15, 6, 17, 14, 9, 11, 3, 4, 13, 2]
    for i in set_of_nodes:
        fila.enqueue(i)

    fila.print_queue()
