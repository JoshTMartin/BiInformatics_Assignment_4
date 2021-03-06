# Josh Martin, worked with Federico and Pat

import scipy
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import scipy.cluster.hierarchy as sch
from matplotlib.pyplot import legend
from sklearn.cluster import AgglomerativeClustering

# Extracting the data from the csv file
from sklearn.utils import graph


data = pd.read_csv("input.csv", delimiter=';', header=None, decimal=",")
number_cluster = data.loc[0,0]
elements = data.loc[1,0]
print(data)

array = data.to_numpy()
X = array[2:20,:]
num_elem = len(X)+1
area = np.pi*3


# Performing Scatter plot for data X

labels = range(1,num_elem)
plt.figure(figsize=(11,8))
plt.style.use('seaborn')
plt.subplots_adjust(bottom=0.1)

# Pimping out my scatter... looks so dope..

plt.scatter(X[:,0],X[:,1], s=100, label='Data plots', cmap="c",
            edgecolors='c', linewidths=2, marker='$\heartsuit$')
plt.title('Scatter Plot')
plt.xlabel('X coords')
plt.ylabel('Y coords')

for label, x, y in zip(labels, X[:, 0], X[:, 1]):
    l1 = plt.annotate(
        label,
        xy=(x,y),xytext=(-3,3),
        textcoords='offset points', ha='right', va='bottom')

# legend display

plt.legend(loc=1, shadow=bool)

# Aggiomerative hierarchical algorithm & dendrogram

# Clustering xy data points from scatterplot

plt.figure()
clustering = AgglomerativeClustering(n_clusters = int(number_cluster),
                                     affinity = 'euclidean', linkage ='ward')
clustering.fit_predict(X)
number = clustering.labels_
number = number+1
print(number)
plt.scatter(X[:, 0], X[:, 1], c= clustering.labels_, s=80, cmap='rainbow', marker='x',
            label='Data points', linewidths=3)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Points Clustered')


# Dendrogram of clustered data points

linked = sch.linkage(X, method='ward')
labelList = range(1,num_elem)
plt.figure(figsize=(10,7))
plt.title('Input data for Dendrogram')
plt.xlabel('Scatter plot points')
plt.ylabel('Euclidean Distance')

sch.dendrogram(linked,
               orientation='top',
               distance_sort='descending',
               color_threshold=0.75,            # 4 colours for the leafs
               labels=labelList,
               show_leaf_counts=True)

# Legend for Dendrogram

# Group1 = X[:,0])
# Group2 = plt.plot(X[:,1])
# plt.legend(handles=[Group1, Group2],
#            labels=['Line', 'Group1', 'Group2'])
plt.show()
