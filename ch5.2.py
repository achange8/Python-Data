import scipy.cluster.hierarchy as hclst
from matplotlib import pyplot as plt

data = [[1, 2], [3, 1], [2, 3], [3, 6], [4, 6], [7, 2], [7, 4]]

for no, d in enumerate(data):
    print("No = ", no, ", data = ", d)


methods = ["complete", "ward"]
plt.suptitle("Dendrogram of Hierarchy Clustering")
for i in range(len(methods)):
    plt.subplot(1, 2, i + 1)
    results = hclst.linkage(data, method=methods[i], metric='euclidean')
    hclst.dendrogram(results)
    plt.title(methods[i])
    plt.xlabel("data number")
    plt.ylabel("distance")
plt.show()
