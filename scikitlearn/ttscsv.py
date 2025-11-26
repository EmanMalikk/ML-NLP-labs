from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

# Read the Iris dataset from a CSV file
iris = pd.read_csv("iris.data.csv")

# Assuming the dataset has features in columns 0 to 3 and the target in column 4
x = iris.iloc[:, :4]
y = iris.iloc[:, 4]

# Training split
# For 80% training and 20% testing
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

# For 70% training and 30% testing
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

# For 60% training and 40% testing
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.6)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

# Testing split
# For 80% testing and 20% training
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

# For 70% testing and 30% training
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

# For 60% testing and 40% training
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

# Uncomment the following lines if you want to use them
# print(np.mean(x_train))
# print(np.mean(x_test))
# print(np.mean(y_train))
# print(np.mean(y_test))