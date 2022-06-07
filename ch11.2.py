import MeCab
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

docs = []
texts = []
txt = ""
docno = []

for i in range(0, 10):
    tagger = MeCab.Tagger()
    f = open(f"./newsfile/newsfile{i+1}.txt", 'r', encoding='utf-8')

    texts.append(f.readline())

    node = tagger.parseToNode(texts[i])
    while node:
        node_features = node.feature.split(",")
        if node_features[0] == "名詞" and (node_features[1] == "一般" or node_features[1] == "固有名詞"):
            txt = txt + " " + node.surface
        node = node.next
    docs.append(txt)
    docno.append(f"文書{i}")
    print(f"txtfile num : {i+1} parse done")
    txt = ""

print("文書集合=")
for doc in docs:
    print(doc)

npdocs = np.array(docs)
vectorizer = TfidfVectorizer(norm=None, smooth_idf=False)
vecs = vectorizer.fit_transform(npdocs)

tfidfs = vecs.toarray()
similarity = cosine_similarity(tfidfs)

print("文書No", end='')
for n in docno:
    print("%6s  " % n, end='')
print()
for n, simi in zip(docno, similarity):
    print("%s" % n, end='')
    for s in simi:
        print("%10.4f" % s, end='')
    print()
