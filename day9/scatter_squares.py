#! /usr/bin/env python3
#! _*_ coding: utf-8 _*_

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# 设置绘图窗口大小
plt.figure(figsize=(10, 6))

plt.scatter(x_values, y_values, c=y_values,
            cmap=plt.cm.Blues, edgecolor='none', s=40)

# 设置图表标题、坐标轴标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.axis([0, 1100, 0, 1100000])

plt.show()
