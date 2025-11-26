from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X,y = load_iris(return_X_y=True)
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.7)
dt= DecisionTreeClassifier()

dt.fit(X_train,y_train)
acc_te=dt.score(X_test,y_test)
acc_tr=dt.score(X_train,y_train)

print("train accuracy")
print(round(acc_tr,2)*100)

print("test accuracy")
print(round(acc_te,2)*100)