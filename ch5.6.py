import scipy.cluster.hierarchy as hclst

data = [[1, 2], [3, 1], [2, 3], [3, 6], [4, 6], [7, 2], [7, 4]]
print("Data:")
for no, d in enumerate(data):
    print("no=", no, "data=", d)
print(f"no = {no},data = {len(data)}")

results = hclst.linkage(data, method='single', metric='euclidean')
print("Results:")
for res in results:
    print(res)

cluster_tree = [x for x in range(len(data))]
clusters = [x for x in range(len(data))]

choice_no = 9
parent_no = 0
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
        if a == choice_no or b == choice_no:
            num += n + 1

        if a == num or b == num:
            parent_no = no + n + 1
        else:
            parent_no = num
        cluster_tree.append((c, d))
        clusters.remove(c)
        clusters.remove(d)
        clusters.append((c, d))
        print(">>>> n=", n,  "number of clusters=",
              len(clusters), "clusters=", clusters)
        n += 1
print(f"与えられたデータ={choice_no}番")
print(f"そのクラスタの番号＝{num}")
print(f"その上位のクラスタの番号＝{parent_no}番")
