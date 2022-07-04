import scipy.cluster.hierarchy as hclst
from matplotlib import pyplot as plt

data = [[0, 1], [1, 0], [2, 3], [5, 3], [5, 5]]

for no, d in enumerate(data):
    print("No = ", no, ", data = ", d)

results = hclst.linkage(data, method='ward', metric='euclidean')
hclst.dendrogram(results)
plt.title("Dendrongram of Clustering")
plt.xlabel("data number")
plt.ylabel("distance")

plt.show()
