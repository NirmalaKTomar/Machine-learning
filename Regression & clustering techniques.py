# -*- coding: utf-8 -*-
"""
#Linear Regression <br/>
"""

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures

"""Load and return **boston house price dataset* """

from sklearn.datasets import load_boston
X, y = load_boston(return_X_y=True)

X.shape

y[:5]

"""Splitting the data into training and testing data"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25) 
print(X_train.shape,X_test.shape,y_train.shape,y_test.shape)

# creating an object of LinearRegression
regr = LinearRegression()

#training data
regr.fit(X_train, y_train) 
y_pred = regr.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test,y_pred))
r2 = r2_score(y_test,y_pred)
print(rmse)
print(r2)

fig,ax = plt.subplots()
ax.scatter(y_test,y_pred)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()

polynomial_features= PolynomialFeatures(degree=2)
x_poly = polynomial_features.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(x_poly, y, test_size = 0.25) 
print(X_train.shape,X_test.shape,y_train.shape,y_test.shape)

model = LinearRegression()
model.fit(X_train, y_train)
y_poly_pred = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test,y_poly_pred))
r2 = r2_score(y_test,y_poly_pred)
print(rmse)
print(r2)

fig,ax = plt.subplots()
ax.scatter(y_test,y_poly_pred)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()

from sklearn import datasets

"""#LOGISTIC REGRESSION<br/>

</br></br>Load iris dataset """

iris = datasets.load_iris()

# Create feature matrix
X = iris.data

# Create target vector
y = iris.target

# View the first observation's feature values
X[0]

from sklearn.linear_model import LogisticRegression
regr=LogisticRegression()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25) 
print(X_train.shape,X_test.shape,y_train.shape,y_test.shape)

regr.fit(X_train,y_train)

print(regr.score(X_test,y_test))
predict = regr.predict(X_test)

"""#K-MEANS CLUSTERING <br/>
"""

from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

X = iris.data[:, :2]

plt.scatter(X[:,0], X[:,1], c=y, cmap='gist_rainbow')
plt.xlabel('Sepa1 Length', fontsize=18)
plt.ylabel('Sepal Width', fontsize=18)

km = KMeans(n_clusters = 3, random_state=21)
km.fit(X)

centers = km.cluster_centers_
print(centers)

#this will tell us to which cluster does the data observations belong.
new_labels = km.labels_
# Plot the identified clusters and compare with the answers
fig, axes = plt.subplots(1, 2, figsize=(16,8))
axes[0].scatter(X[:, 0], X[:, 1], c=y, cmap='gist_rainbow',edgecolor='k', s=150)

axes[1].scatter(X[:, 0], X[:, 1], c=new_labels, cmap='jet',
edgecolor='k', s=150)
axes[1].scatter(centers[:,0],centers[:,1],c='r',marker='x')

axes[0].set_xlabel('Sepal length', fontsize=10)
axes[0].set_ylabel('Sepal width', fontsize=10)
axes[1].set_xlabel('Sepal length', fontsize=10)
axes[1].set_ylabel('Sepal width', fontsize=10)
axes[0].tick_params(direction='in', length=10, width=5, colors='k', labelsize=10)
axes[1].tick_params(direction='in', length=10, width=5, colors='k', labelsize=10)
axes[0].set_title('Actual', fontsize=10)
axes[1].set_title('Predicted', fontsize=10)
