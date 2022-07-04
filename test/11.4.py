# TF-IDFを計算
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

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

# 単語帳を表示
terms = vectorizer.get_feature_names()
print("単語文書行列（TF-IDF)=")
print("単語\t", end='')
for term in terms:
    print("%6s" % term, end='')
print()

# TF-IDFを計算
tfidfs = vecs.toarray()
# 計算結果を表示
for n, tfidf in enumerate(tfidfs):
    print("文書", n, "\t", end='')
    for t in tfidf:
        print("%8.4f" % t, end='')
    print()
