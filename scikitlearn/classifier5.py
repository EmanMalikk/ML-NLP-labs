from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
X,y = load_iris(return_X_y=True)

nb= GaussianNB()
nb_cv=cross_val_score(nb,X,y,cv=7)

#percentage
percentage=nb_cv*100
print(percentage)

#mean
print("mean")
print(percentage.mean())

#standard deviation
print("std")
print(nb_cv.std())

