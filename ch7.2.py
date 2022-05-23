from pyexpat import model
from sklearn import datasets
from sklearn import model_selection
from sklearn import naive_bayes
from sklearn import metrics

size = [0.2, 0.4, 0.6, 0.8]
for i in range(len(size)):
    print("size = ", size[i])
    iris = datasets.load_iris()
    data_train, data_test, label_train, label_test = model_selection.train_test_split(
        iris['data'], iris['target'], test_size=size[i])

    model = naive_bayes.GaussianNB().fit(data_train, label_train)

    y_true = label_test
    y_pred = model.predict(data_test)
    print("真ラベル =", y_true)
    print("予測ラベル =", y_pred)

    print("精度 =", metrics.accuracy_score(y_true, y_pred))
    print(metrics.classification_report(
        y_true, y_pred, target_names=iris['target_names']))
