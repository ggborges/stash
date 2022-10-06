import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

n_samples = 200
blob_centers = ([1,1], [3,4], [1, 3.3], [3.5, 1.8])
data, labels = make_blobs(n_samples=n_samples,
                          centers=blob_centers,
                          cluster_std=0.5,
                          random_state=0)

colours = ('green', 'orange', 'blue', 'magenta')
fig, ax = plt.subplots()

for n_class in range(len(blob_centers)):
    ax.scatter(data[labels==n_class][:, 0],
               data[labels==n_class][:, 1],
               c=colours[n_class],
               s=30,
               label=str(n_class))

datasets = train_test_split(data, labels, test_size=0.2)

train_data, test_data, train_labels, test_labels = datasets

clf = MLPClassifier(solver='lbfgs',
                    alpha=1e-5,
                    hidden_layer_sizes=(6,),
                    random_state=1)

clf.fit(train_data, train_labels)

clf.score(train_data, train_labels)


