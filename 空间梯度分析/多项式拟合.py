import pandas as pd
import matplotlib.pyplot as plt

#create DataFrame
df = pd.DataFrame({
    'x':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
    'y':[3,14,23,25,23,15,9,5,9,13,17,24,32,36,46]
})

#create sctterplot of x vs. y


import numpy as np

#fit polynomial models up to degree 5
model1 = np.poly1d(np.polyfit(df.x, df.y, 1))
model2 = np.poly1d(np.polyfit(df.x, df.y, 2))
model3 = np.poly1d(np.polyfit(df.x, df.y, 3))
model4 = np.poly1d(np.polyfit(df.x, df.y, 4))
model5 = np.poly1d(np.polyfit(df.x, df.y, 5))

#create scatterplot
polyline = np.linspace(1, 15, 50)
plt.scatter(df.x, df.y)

#add fitted polynomial lines to scatterplot
'''
plt.plot(polyline, model1(polyline), color='green')
plt.plot(polyline, model2(polyline), color='red')
plt.plot(polyline, model3(polyline), color='purple')
plt.plot(polyline, model4(polyline), color='blue')
plt.plot(polyline, model5(polyline), color='orange')
plt.show()
'''

def adjR(x,y,degree):
    results = {}
    coeffs = np.polyfit(x, y, degree)
    p = np.poly1d(coeffs)
    yhat = p(x)
    ybar = np.sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)
    sstot = np.sum((y - ybar)**2)
    results['r_squared'] = 1- ((1 - (ssreg-sstot)*(len(y) - 1))/(len(y) - degree - 1))

    return results

#calculated adjusted R-squared of each model
print(
adjR(df.x, df.y, 1),
adjR(df.x, df.y, 2),
adjR(df.x, df.y, 3),
adjR(df.x, df.y, 4),
adjR(df.x, df.y, 5)
)

#fit fourth-degree polynomial
model = np.poly1d(np.polyfit(df.x, df.y, 4))

#define scatterplot
polyline = np.linspace(1, 15, 50)
plt.scatter(df.x, df.y)

#add fitted polynomial curve to scatterplot
plt.plot(polyline, model4(polyline), '--', color='red')
plt.show()