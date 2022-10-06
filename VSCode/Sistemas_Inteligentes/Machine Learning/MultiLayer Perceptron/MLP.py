import random
import numpy as np

'''
    Neste código, o parâmetro sizes contêm o número de neurônios nas respectivas camadas, 
sendo um objeto do tipo lista em Python. Então, por exemplo, se queremos criar um objeto
da classe Network com 2 neurônios na primeira camada, 3 neurônios na segunda camada
e 1 neurônio na camada final, aqui está o código que usamos para instanciar um objeto da classe Network:

    rede1 = Network([2,3,1])

    Os bias e pesos no objeto rede1 são todos inicializados aleatoriamente, usando a função Numpy np.random.randn
para gerar distribuições gaussianas com 0 de média e desvio padrão 1.
    Esta inicialização aleatória dá ao nosso algoritmo de descida do gradiente estocástico um local para começar.
'''

class Network(object):

    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
    
    # função de ativação (activation function)
    def sigmoid(z):
        return 1.0/(1.0+np.exp(-z))

    def feedforward(self, a):
        
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a) + b)
        
        return a

    # Stochastic Gradient Descent
    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None): # eta = taxa de aprendizagem / test_data: opicional
        
        training_data = list(training_data)
        n = len(training_data)

        if test_data:
            test_data = list(test_data)
            n_test = len(test_data)

        for j in range(epochs):
            random.shuffle(training_data)
            mini_batches = [training_data[k:k+mini_batch_size] for k in range(0, n, mini_batch_size)]

            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)

            if test_data:
                print("Epoch {} : {} / {}".format(j,self.evaluate(test_data),n_test))
            else:
                print("Epoch {} finalizada.".format(j))
    
    def update_mini_batch(self, mini_batch, eta):

        pass