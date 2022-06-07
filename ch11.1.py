from pydoc import doc
import MeCab
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

docs = []
texts = []
txt = ""
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
    print(f"txtfile num : {i+1} parse done")

    txt = ""

print("文書集合=")
for doc in docs:
    print(doc)

npdocs = np.array(docs)
vectorizer = TfidfVectorizer(norm=None, smooth_idf=False)
vecs = vectorizer.fit_transform(npdocs)

terms = vectorizer.get_feature_names()
print("単語文書行列(TF-IDF)=")
print("単語\t", end='')
for term in terms:
    print("%6s" % term, end='')
print()

tfidfs = vecs.toarray()
for n, tfidf in enumerate(tfidfs):
    print("文書", n, "\t", end='')
    for t in tfidf:
        print("%8.4f" % t, end='')
    print()
