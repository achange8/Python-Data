# 文書間の類似度
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#　文書集合
docs = [
    '温暖化 温暖化 地球 日本 地球 地球',
    '天気 日本 水温 太平洋 日本 水温',
    '太平洋 水温 日本 温暖化 水温',
]
print("文書集合=")
for doc in docs:
    print(doc)

# オブジェクト生成
npdocs = np.array(docs)
vectorizer = TfidfVectorizer(norm=None, smooth_idf=False)
vecs = vectorizer.fit_transform(npdocs)
# TF-IDF
tfidfs = vecs.toarray()
# コサイン類似度
similarity = cosine_similarity(tfidfs)

# 計算結果を表示
docno = ["文書0", "文書1", "文書2"]
print("文書No", end='')
for n in docno:
    print("%6s  " % n, end='')
print()
for n, simi in zip(docno, similarity):
    print("%s" % n, end='')
    for s in simi:
        print("%10.4f" % s, end='')
    print()
