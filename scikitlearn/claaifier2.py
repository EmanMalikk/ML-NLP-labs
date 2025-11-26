from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

X,y = load_breast_cancer(return_X_y=True)
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.7)
rf= RandomForestClassifier()

rf.fit(X_train,y_train)
acc_te=rf.score(X_test,y_test)
acc_tr=rf.score(X_train,y_train)

#training accuracy
print("train accuracy")
print(round(acc_tr,2)*100)

#testing accuracy
print("test accuracy")
print(round(acc_te,2)*100)