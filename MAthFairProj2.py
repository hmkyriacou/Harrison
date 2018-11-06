import random
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Import Data
df = pd.read_csv("Housing.csv")

y = df['price']
x = df['lotsize']
#Multy linear regression data
x2 = df['bedrooms']
#tf = df[['lotsize', 'bedrooms']]


x = x.values.reshape(len(x), 1)
y = y.values.reshape(len(y), 1)
#Bedroom reshape
#x2 = x2.values.reshape(len(x2), 1)
#tf = tf.values.reshape(len(tf), 2)

    #Regression code
#train and test data sets
train_data_x = x
test_data_x = x
train_data_y = y
test_data_y = y
#Multy Linear Regression train and test data
#train_data_tf = tf
#test_data_tf = tf

#Multy Linear Regression model
#mregr = linear_model.LinearRegression()
#mregr.fit(train_data_tf, train_data_y)

#Regression model
regr = linear_model.LinearRegression()
regr.fit(train_data_x, train_data_y)

#Calculating the equation of best fit line
m = str(float(regr.coef_))
b = str(float(regr.intercept_))
print('y = ' + m + 'x + ' + b)

#Multy Linear Regression Equation
#m2 = str(float(mregr.coef_[0]))
#b2 = str(float(mregr.intercept_[0]))
#print('y = ' + m2 + 'x + ' + b2)

#Plot Data
plt.scatter(test_data_x, test_data_y, color = 'black')
#plt.scatter(x2, test_data_y, color = 'blue')
plt.plot(test_data_x, regr.predict(test_data_x), color = 'red', linewidth = 3)
#plt.plot(test_data_tf, mregr.predict(test_data_tf), color = 'yellow', linewidth = 3)
#plt.legend(('y = mx+b', 'point'))
plt.title('Linear Regression Example')
plt.show()
