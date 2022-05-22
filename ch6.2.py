import numpy as np
import matplotlib.pyplot as plt
from sklearn import cluster

# data
data = [[1, 2], [3, 1], [2, 3], [3, 6], [4, 6], [7, 2], [7, 4], [5, 4], [5, 5]]
data = np.array(data)

model = cluster.KMeans(n_clusters=4)
model.fit(data)
labels = model.labels_

plt.figure(1)
ldata = data[labels == 0]
plt.scatter(ldata[:, 0], ldata[:, 1], marker='s', color='green')
ldata = data[labels == 1]
plt.scatter(ldata[:, 0], ldata[:, 1], marker='o', color='red')
ldata = data[labels == 2]
plt.scatter(ldata[:, 0], ldata[:, 1], marker='^', color='red')
ldata = data[labels == 3]
plt.scatter(ldata[:, 0], ldata[:, 1], marker='x', color='black')
plt.title("Scatter Plot of Clustered Data")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
