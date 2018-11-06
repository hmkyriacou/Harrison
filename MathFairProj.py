import random
from sklearn import linear_model
import matplotlib.pyplot as plt
def f(x):
    res = x * 25 + 3
    #res = x * 5 + 3
    error = res * random.uniform(-0.01, 0.01)
    return res + error
    #return res
values = []
#for i in range(0, 200):
for i in range(0, 300):
    #x = random.uniform(1, 50)
    x = random.uniform(1, 1000)
    y = f(x)
    values.append((x, y))

x, y = zip(*values)
print(x)
print('-----------------------------------------------------')
print(y)
regr = linear_model.LinearRegression()
min_x = min(x)
max_x = max(x)
train_data_x = list(map(lambda x: [x], list(x[:-20])))
train_data_y = list(y[:-20])
regr.fit(train_data_x, train_data_y)
m = regr.coef_[0]
b = regr.intercept_

plt.scatter(x, y, color='blue')
plt.plot([min_x, max_x], [b, m*max_x + b], 'r')
#plt.plot()
plt.title('Linear Random Data', fontsize=13)
plt.text(300, 20000, 'y = {0} * x + {1}'.format(round(m, 4), round(b, 4)))
plt.show()

print('\ny = {0} * x + {1}'.format(round(m, 4), round(b, 4)))
