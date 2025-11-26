from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import numpy as np

x,y= load_breast_cancer (return_X_y=True)

#training split
#for 80% training and 20% testing
print(train_test_split(x,y,train_size=0.8))

#for 70% training and 30% testing
print(train_test_split(x,y,train_size=0.7))


#for 60% training and 40% testing
print(train_test_split(x,y,train_size=0.6))

#testing split
#for 80% testing and 20% training
print(train_test_split(x,y,test_size=0.2))

#for 70% testing and 30% training
print(train_test_split(x,y,test_size=0.3))

#for 60% testing and 40% training
print(train_test_split(x,y,test_size=0.4))

#.shape

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_train.shape)

#mean values
print(np.mean(x_train))
print(np.mean (x_test))
print(np.mean (y_train))
print(np.mean( y_train))