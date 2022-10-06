from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from matplotlib import RcParams, pyplot as plt
from pylab import rcParams
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

# Lendo e obtendo informações básicas

df = pd.read_csv('C:/Users/VAIO/Documents/Guga/VSCode/Sistemas_Inteligentes/Machine Learning/kNN/iris.data', header = None)
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

print(df.head())

print('\n' + str(df.describe().T))

'''
Pré-processando

    Convertendo as classes para números
'''
# Label Encoder é uma classe que codifica valores categóricos (textuais) em valores numéricos
le = preprocessing.LabelEncoder() # Somente para rótulos, nunca para atributos
# Apesar de que o kNN não necessite fazer essa conversão,
# uma vez que ele não faz nenhuma operação com esses valores
# apenas assume o valor de maior repetição dentre os K vizinhos
y = le.fit_transform(df['class']) # Transforma os valores categóricos em numéricos e guarda em um array
# método fit_transform() ajusta e transforma os dados internos do nosso codificador

print("\n<<<<<<>>>>>>\n\nList(df['class']):\n" + str(list(df['class'])) + '\n')
x = df.drop(['class'], axis=1).to_numpy()

print('<<<<<<>>>>>>\n\ny:\n' + str(y) + '\n\n')
print('<<<<<<>>>>>>\n\nx:\n' + str(x) + '\n\n')

# Dividindo em treino, validação e teste
'''
Validação consiste na busca pelos melhores valores de parâmetros, ou seja, aquele conjunto de valores que maximizam a performance do modelo.

Para tal, separa-se uma parte do dataset de treino como sub-conjunto de avaliação/validação do modelo. 
Então, treina-se com o novo dataset de treino e avalia-se com de validação.

Nunca deve-se validar um modelo usando o dataset de teste.

O desempenho final do modelo deve ser avaliado treinando-se com o dataset de treinamento original e o dataset de teste.
'''
# y -> um array com os valores numéricos referentes as classes categóricas
# x -> array com as demais colunas da base de dados (atributos)

SEED = 4

# Divisão de entre data set de treino e de teste
X_train, X_test, y_train, y_test = train_test_split(x, y, 
                                                    test_size = 0.15, # 15% da base de dados para teste
                                                    random_state = SEED, 
                                                    stratify=y) # Stratify configura uma divisão estratificada, mantém a proporção de classes original
print('\n\n°°°°°°°°°°°°°°\nX_train: ' + str(X_train))
print('\nX_test: ' + str(X_test))
print('\ny_train: ' + str(y_train))
print('\ny_test: ' + str(y_test))

# Já com o data set de treino definido,
# dividimos mais uma vez, esse data set de treino,
# em data set de treino e data set de validação
X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, 
                                                      test_size = 0.10, # 10% da base de dados para validação
                                                      random_state = SEED, 
                                                      stratify=y_train)
print('\n\n°°°°°°°°°°°°°°\nX_train: ' + str(X_train))
print('\nX_valid: ' + str(X_valid))
print('\ny_train: ' + str(y_train))
print('\ny_valid: ' + str(y_valid))

X_train = preprocessing.maxabs_scale(X_train)
X_valid = preprocessing.maxabs_scale(X_valid)
X_test = preprocessing.maxabs_scale(X_test)

print('\n\n°°°°°°°preprocessing°°°°°°°\nX_train: ' + str(X_train))
print('\nX_valid: ' + str(X_valid))
print('\nX_test: ' + str(X_test))

# Treinando o modelo para vários Ks [SPLIT único]

k_range = range(1,51)
k_scores_train = []
k_scores_valid = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)

    k_scores_train.append(knn.score(X_train, y_train)) # Acurácia
    k_scores_valid.append(knn.score(X_valid, y_valid))

# Plotando a curva de acurácia

# plt.rcParams["figure.figsize"] = [7.50, 3.50]
#<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>
plt.rcParams['figure.autolayout'] = True # NÃO ENTENDI O FUNCIONAMENTO DESSA LINHA


fig, ax = plt.subplots(figsize=(10,8))
ax.set_xlabel("K")
ax.set_ylabel("Accuracy")
ax.set_title("Accuracy score vs K")
ax.plot(k_range, k_scores_train, marker='o', label="training")
ax.plot(k_range, k_scores_valid, marker='o', label="validation")

for k, t, v in zip(k_range, k_scores_train, k_scores_valid):
    if k % 2 == 0:
        plt.text(k, t, k)
        plt.text(k, v, k)

ax.legend()
plt.show()

# Avaliando o modelo com o melhor K
        # Abaixo, recupero o valor de K segundo o melhor valor de acurácio de validação

best_values = max(zip(k_range, k_scores_train, k_scores_valid), key=lambda v:v[-1])
print('\n\n<<<<<<<<<<<<<Avaliando o modelo com o melhor K>>>>>>>>>>>>>\nbest_values:\n' + str(best_values))
best_k, best_acc_train, best_acc_valid = best_values
print('best_k, best_acc_train, best_acc_valid:\n', best_k, best_acc_train, best_acc_valid)

knn = KNeighborsClassifier(n_neighbors=best_k)
knn.fit(X_train+X_valid, y_train+y_valid) # X_train + X_valid

print("Acurácia de treino: ", knn.score(X_train, y_train))
print("Acurácia de validação: ", knn.score(X_valid, y_valid))
print("Acurácia de teste: ", knn.score(X_test, y_test))

'''
Gráfico de dispersão do datasets

Como plotar dados N-Dimensionais?

Podemos fazer isso reduzindo as dimensões para o espaço bi ou tridimensional.

Existem diversas técnicas dedicas a esta tarefa, algumas das quais são o PCA, t-SNE e UMAP.
Aqui utilizaremos o PCA, que é suportado pelo scikit.
'''

pca = PCA(n_components=2)
X_pca = pca.fit_transform(preprocessing.maxabs_scale(x)) # Processando a base da dados completa

colors = ['tab:blue', 'tab:orange', 'tab:green']

fig, ax = plt.subplots(figsize=(10,8))
classes = le.inverse_transform(sorted(set(y)))

for i, color in enumerate(colors):
  ax.scatter(X_pca[y==i, 0], 
             X_pca[y==i, 1], 
             label=classes[i], 
             color = color, 
             alpha=.5, s = 200)

plt.legend()
ax.grid(True)
plt.show()