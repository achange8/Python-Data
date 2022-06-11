from sklearn import datasets
from sklearn import model_selection
from sklearn import svm
from sklearn import metrics

digits = datasets.load_digits()
data_train, data_test, label_train, label_test = model_selection.train_test_split(
    digits['data'], digits['target'], test_size=0.25)
targetnames = []
for name in digits['target_names']:
    targetnames.append(str(name))

C = 1000
gamma = 0.1
model = svm.SVC(C=C, gamma=gamma)
model.fit(data_train, label_train)

label_train_pred = model.predict(data_train)
label_test_pred = model.predict(data_test)

print("訓練データによる評価:")
print("精度 =", metrics.accuracy_score(label_train, label_train_pred))
print(metrics.classification_report(label_train,
      label_train_pred, target_names=targetnames))
print()
print("テストデータによる評価:")
print("精度 =", metrics.accuracy_score(label_test, label_test_pred))
print(metrics.classification_report(label_test,
      label_test_pred, target_names=targetnames))
