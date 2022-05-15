from secrets import choice
import scipy.cluster.hierarchy as hclst

data = [[1, 2], [3, 1], [2, 3], [3, 6], [4, 6], [7, 2], [7, 4]]
print("Data:")
for no, d in enumerate(data):
    print("no=", no, "data=", d)

results = hclst.linkage(data, method='single', metric='euclidean')
print("Results:")
for res in results:
    print(res)

cluster_tree = [x for x in range(len(data))]
clusters = [x for x in range(len(data))]

choice_no = 3
other_no = 0
num = no
n = 0
distance_max = 6
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
        if a == choice_no or b == choice_no:
            num += n + 1
            if a == choice_no:
                other_no = int(b)
            else:
                other_no = int(a)
        clusters.remove(c)
        clusters.remove(d)
        clusters.append((c, d))
        print(">>>> n=", n,  "number of clusters=",
              len(clusters), "clusters=", clusters)
        n += 1
print(f"与えられたデータ={choice_no}番")
print(f"そのクラスタの番号＝{num}")
print(f"そのクラスタにあるほかのデータ＝{other_no}番")
