from secrets import choice
import scipy.cluster.hierarchy as hclst

data = [
    [0, 1],
    [1, 0],
    [2, 3],
    [5, 3],
    [5, 5],
]
num = len(data)
print("Data:")
for no, d in enumerate(data):
    print("no=", no, "data=", d)

results = hclst.linkage(data, method='single', metric='euclidean')

print("Results:")
for res in results:
    print(res)

cluster_tree = [x for x in range(len(data))]
clusters = [x for x in range(len(data))]
n = 0
distance_max = 10
print("Clusters:")
for a, b, distance, represent in results:
    if distance <= distance_max:
        print("a=", int(a), "b=", int(b), distance, represent)
        if(int(a) >= len(data)):
            c = cluster_tree[int(a)]
        else:
            c = int(a)
        if(int(b) >= len(data)):
            d = cluster_tree[int(b)]
        else:
            d = int(b)
        cluster_tree.append((c, d))
        clusters.remove(c)
        clusters.remove(d)
        clusters.append((c, d))
        if(distance < distance_max):
            num += 1
        print(">>>> n=", n,  "number of clusters=",
              len(clusters), "clusters=", clusters)
        n += 1
print(f"distance_max={distance_max}")
print(f"直近のクラスタの番号は{num-1}です")
