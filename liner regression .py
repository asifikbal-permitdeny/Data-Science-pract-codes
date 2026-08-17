# y=b0+x1*b1

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

data = pd.read_excel('dataset.xlsx')

print(data)

print(data.describe())

y=data['GPA']
x1=data['SAT']

plt.scatter(x1,y)
plt.xlabel('SAT',fontsize=30)
plt.ylabel('GPA',fontsize=30)
plt.show()


x = sm.add_constant(x1)
model = sm.OLS(y, x)
results = model.fit()

predicted = results.predict(x)

plt.scatter(x1, y)
plt.plot(x1, predicted)
plt.xlabel('SAT')
plt.ylabel('GPA')
plt.show()


