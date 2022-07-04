import pandas as pd  # 데이터프레임 사용을 위해
from math import log  # IDF 계산을 위해

docs = [
    '温暖化 温暖化 地球 日本 地球 地球',
    '天気 日本 水温 太平洋 日本 水温',
    '太平洋 水温 日本 温暖化 水温'
]
vocab = list(set(w for doc in docs for w in doc.split()))
vocab.sort()
# 총 문서의 수
N = len(docs)


def tf(t, d):
    return d.count(t)


def idf(t):
    df = 0
    for doc in docs:
        df += t in doc
    return log(N/(df+1))


def tfidf(t, d):
    return tf(t, d) * idf(t)


result = []

# 각 문서에 대해서 아래 연산을 반복
for i in range(N):
    result.append([])
    d = docs[i]
    for j in range(len(vocab)):
        t = vocab[j]
        result[-1].append(tf(t, d))

tf_ = pd.DataFrame(result, columns=vocab)

result = []
for i in range(N):
    result.append([])
    d = docs[i]
    for j in range(len(vocab)):
        t = vocab[j]
        result[-1].append(tfidf(t, d))

tfidf_ = pd.DataFrame(result, columns=vocab)
