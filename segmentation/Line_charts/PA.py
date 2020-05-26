import numpy as np
import matplotlib.pyplot as plt

#1-cascaded
x1 = np.linspace(0, 1, 5)
y1 = x1

plt.figure()
plt.plot(x1, y1, color='blue', marker='v', label="1-Cascaded")
#2-cascaded
x2 = np.linspace(0, 1, 5)
y2 = 2 * x2
plt.plot(x2, y2, color='red', marker='*', label="2-Cascaded")


#3-cascaded
x3 = np.linspace(0, 1, 5)
y3 = 3 * x3
plt.plot(x3, y3, color='green', marker='o', label="3-Cascaded")

#4-cascaded
x4 = np.linspace(0, 1, 5)
y4 = 4 * x4
plt.plot(x4, y4, color='c', marker='<', label="4-Cascaded")


plt.xlabel("Iteration (K)")
plt.ylabel("PA (%)")
plt.title("AP Comparison")
plt.legend()
plt.show()
