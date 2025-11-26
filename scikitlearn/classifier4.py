from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
X,y = load_diabetes(return_X_y=True)
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.7)
gb= GaussianNB()
gb.fit(X_train,y_train)

acc_te=gb.score(X_test,y_test)
acc_tr=gb.score(X_train,y_train)

print("train accuracy")
print(round(acc_tr,2)*100)

print("test accuracy")
print(round(acc_te,2)*100)