# wikiデータのTFIDFを計算する
import MeCab
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

tagger = MeCab.Tagger()


def read_wikidata(filename):
    wikifile = open(filename, "r", encoding="utf_8")
    tagger = MeCab.Tagger('-Ochasen')
    buf = []
    docdone = False
    titles = []
    documents = []
    doccnt = 0

    for line in wikifile:
        if line.startswith('<doc '):
            buf = []
            docdone = False
            m = re.search('title=.*>', line)
            title = m.group().replace('title="', '')
            title = title.replace('">', '').strip()

        elif line.startswith('</doc>'):
            doc = ''.join(buf)
            docdone = True
            doccnt += 1
        else:
            if len(line) != 0:
                buf.append(line)

        words = ""
        if docdone == True:
            node = tagger.parseToNode(doc)
            while node:
                node_features = node.feature.split(",")
                if node_features[0] == "名詞" and (node_features[1] == "一般" or node_features[1] == "固有名詞"):
                    words = words+" "+node.surface
                node = node.next

        if len(words) >= 100:
            titles.append(title)
            documents.append(words)

    return(titles, documents)


def calculate_tfidf(titles, docs):
    npdocs = np.array(docs)
    vectorizer = TfidfVectorizer(norm=None, smooth_idf=False)
    vecs = vectorizer.fit_transform(npdocs)
    terms = vectorizer.get_feature_names()
    tfidfs = vecs.toarray()
    pp = {}
    for n, tfidf in enumerate(tfidfs):
        print("文書番号=", n, "タイトル=", titles[n], ">>>", end='')
        print()
        for i, _ in enumerate(terms):
            pp[f"{terms[i]}"] = tfidf[i]
        for key, velue in sorted(pp.items(), key=lambda x: x[1], reverse=True)[0:5]:
            print(key,  velue)
        print()

    return tfidfs


wikifilename = "./wikidata/wikiarticles/AA/wiki_00"
wikititles, wikidocuments = read_wikidata(wikifilename)
wikitfidfs = calculate_tfidf(wikititles, wikidocuments)
