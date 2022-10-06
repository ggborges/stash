import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
from matplotlib import RcParams, rcParams
rcParams["figure.figsize"] = 10, 5


#normalize or standardize data prior to using the model

df = pd.read_csv('C:/Users/VAIO/Documents/Guga/VSCode/Sistemas_Inteligentes/Machine Learning/kNN/iris.data', header=None)
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

print(df.head())

print('\n' + str(df.describe().T))

le = preprocessing.LabelEncoder()

# Dividindo entre as features e as classes
y = le.fit_transform(df['class'])

print("\n<<<<<<>>>>>>\n\nList(df['class']):\n" + str(list(df['class'])) + '\n')
print(y)

X = df.drop(['class'], axis=1).to_numpy()

print(X)

SEED = 0

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=SEED, stratify=y)

print('\n\n°°°°°°°°°°°°°°\nX_train: ' + str(X_train))
print('\nX_test: ' + str(X_test))
print('\ny_train: ' + str(y_train))
print('\ny_test: ' + str(y_test))

# standardize the data using the 'StandarScalar'

# create instance
sc = StandardScaler()

# fit the scaler to the training feature set ONLY
sc.fit(X_train)

# scale (transform) the training AND the testing sets
# using the scaler that was fitted to training data
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# it is important 