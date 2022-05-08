import scipy.cluster.hierarchy as hclst
from matplotlib import pyplot as plt

data = [[1, 2], [3, 1], [2, 3], [3, 6], [4, 6], [7, 2], [7, 4], [5, 4]]

for no, d in enumerate(data):
    print("No = ", no, ", data = ", d)

results = hclst.linkage(data, method='ward', metric='euclidean')
hclst.dendrogram(results)
plt.title("Dendrongram of Clustering")
plt.xlabel("data number")
plt.ylabel("distance")

plt.show()
