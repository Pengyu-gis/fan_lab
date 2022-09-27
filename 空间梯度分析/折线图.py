# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt


names = (10,20, 30, 40)
x = range(len(names))


y_1 = [-333, -65, 28, 716]
y_2 = [186, 492, 142, 1498]
# y_3 = [4, 5, 6, 1, 2, 3]

plt.plot(x, y_1, color='orangered', marker='o', linestyle='-', label='popH')
plt.plot(x, y_2, color='blueviolet', marker='D', linestyle='-.', label='popR')
# plt.plot(x, y_3, color='green', marker='*', linestyle=':', label='C')
plt.legend()  # 显示图例
plt.xticks(x, names, rotation=45)
plt.xlabel("X")  # X轴标签
plt.ylabel("Y")  # Y轴标签
plt.show()