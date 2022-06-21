import MeCab
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import datetime

# 形態素解析器
tagger = MeCab.Tagger()

# Read wiki data


def read_wikidata(filename):
    wikifile = open(filename, "r", encoding="utf_8")
    tagger = MeCab.Tagger()
    buf = []
    docdone = False
    titles = []
    documents = []
    doccnt = 0
    print("Read file start")
    # Read the file and process one line at a time
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
    print("Read file done")
    return(titles, documents)


def calculate_tfidf(titles, docs):
    # オブジェクト生成
    npdocs = np.array(docs)
    vectorizer = TfidfVectorizer(norm=None, smooth_idf=False)
    vecs = vectorizer.fit_transform(npdocs)
    # TF-IDF
    tfidfs = vecs.toarray()
    # 単語帳を表示
    terms = vectorizer.get_feature_names()
    # TF-IDFを計算
    tfidfs = vecs.toarray()

    return tfidfs

# cos 類似度


def calculate_similarity(titles, tfidfs):
    similarity = cosine_similarity(tfidfs)
    for n1, simi in enumerate(similarity):
        print("-------文書1 = %d   タイトル = %s ----------" % (n1, titles[n1]))
        pp = {}
        for n2, s in enumerate(simi):
            if(n1 != n2 and s >= 0.2):
                pp[f"{titles[n2]}"] = s
        for key, value in sorted(pp.items(), key=lambda x: x[1], reverse=True)[0:3]:
            print("文書1=%s 文書2=%s 類似度=%8.6f" % (titles[n1], key, value))
    return


def main():
    wikifilename = "./wikidata/wikiarticles/AA/wiki_00"
    wikititles, wikidocuments = read_wikidata(wikifilename)
    wikitfidfs = calculate_tfidf(wikititles, wikidocuments)
    calculate_similarity(wikititles, wikitfidfs)


# start
if __name__ == "__main__":
    start_time = datetime.datetime.now()
    main()
    end_time = datetime.datetime.now()
    elapsed_time = end_time-start_time
    print("経過時間=", elapsed_time)
    print("---完了---")
