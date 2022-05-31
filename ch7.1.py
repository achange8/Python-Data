from sklearn import datasets
from sklearn import model_selection
from sklearn import naive_bayes
from sklearn import metrics


for i in range(0, 10):
    print(i, "回目")
    iris = datasets.load_iris()
    data_train, data_test, label_train, label_test = model_selection.train_test_split(
        iris['data'], iris['target'], test_size=0.25)

    model = naive_bayes.GaussianNB().fit(data_train, label_train)

    y_true = label_test
    y_pred = model.predict(data_test)
    print("真ラベル =", y_true)
    print("予測ラベル =", y_pred)

    print("精度 =", metrics.accuracy_score(y_true, y_pred))
    print(metrics.classification_report(
        y_true, y_pred, target_names=iris['target_names']))
