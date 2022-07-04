
import cv2.cv2 as cv
import numpy as np
import datetime
import scipy.cluster
from sklearn.feature_extraction.text import CountVectorizer
import scipy.cluster.hierarchy as hclst
from matplotlib import pyplot as plt
from os.path import join, relpath
import glob


def extract_features():
    #filespath = "./imagedata"
    filespath = "./picturedata"

    print("path = ", filespath)
    filenames = [relpath(x, filespath)
                 for x in glob.glob(join(filespath, '*'))]
    print("files name = ", filenames)
    print("total files = ", len(filenames))
    # read img files
    img = []
    for i, filename in enumerate(filenames):
        img.append(cv.imread(f'{filespath}/{filename}'))

    detector = cv.AKAZE_create()

    kp = []
    des = []
    for i, name in enumerate(img):
        kp, des0 = detector.detectAndCompute(name, None)
        des.append(des0)
    return des

# データをクラスタリング


def create_docs(des):
    desall = np.vstack(des)
    npdesall = np.array(desall, dtype='float64')
    codebook, destortion = scipy.cluster.vq.kmeans(
        npdesall, 100, iter=30, thresh=1e-06)
    # ベクトル量子化
    # 各データをセントロイドに分類する
    codeall = []
    for _, value in enumerate(des):
        code, dist = scipy.cluster.vq.vq(value, codebook)
        codeall.append(code)

    docs = []
    for codes in codeall:
        words = ""
        for code in codes:
            words = words+" "+str(code)
        docs.append(words)

    return docs


def clustering_images(docs):

    npdocs = np.array(docs)
    vectorizer = CountVectorizer()
    vecs = vectorizer.fit_transform(npdocs)
    data = vecs.toarray()
    for no, dd in enumerate(data):
        print("画像番号 =", no)
        print("コードの出現回数データ =")
        for n, d in enumerate(dd):
            if((n+1) % 15 != 0):
                print("%4d" % d, end="")
            else:
                print("%4d" % d)
        print()

    results = hclst.linkage(data, method='ward', metric='euclidean')

    hclst.dendrogram(results)
    plt.title("Dendrogram of Clustering Images")
    plt.xlabel("image number")
    plt.ylabel("distance")
    plt.savefig("ch14ex4Figure1.png")

    return


def main():
    des1 = extract_features()
    docs = create_docs(des1)
    clustering_images(docs)

    return


# start
if __name__ == "__main__":
    start_time = datetime.datetime.now()
    main()
    end_time = datetime.datetime.now()
    elapsed_time = end_time-start_time
    print("経過時間 =", elapsed_time)
    print("すべて完了 !!!")
