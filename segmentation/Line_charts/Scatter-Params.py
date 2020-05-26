import numpy as np
import matplotlib.pyplot as plt

x = [262.1, 118.1, 250.8, 29.5,  63.26, 47.61, 28.6,  49, 26.5, 3.9, 5.8]
y= [63.1 ,73.6 ,81.2 ,57  ,75.2 ,74.2 ,73.2 ,74.7 ,70.6 ,70.7 ,68]
n = np.arange(14)

methods = ["DeepLab", "RefineNet-101", "PSPNet", "SegNet", "CARNet-152", "CARNet-101", "CARNet-50", "BiseNet2", "ICNet", "CARNet-Mobile", "BiseNet1"]


fig, ax = plt.subplots()

ax.invert_xaxis()#  反转

ax.annotate(methods[0], (x[0], y[0]), (x[0]-10, y[0]))
ax.annotate(methods[1], (x[1], y[1]), (x[1]+70, y[1]))
ax.annotate(methods[2], (x[2], y[2]), (x[2]-10, y[2]))
ax.annotate(methods[3], (x[3], y[3]), (x[3]+35, y[3]))
ax.annotate(methods[4], (x[4], y[4]), (x[4]+60, y[4]))
ax.annotate(methods[5], (x[5], y[5]), (x[5]+54, y[5]-1))
ax.annotate(methods[6], (x[6], y[6]), (x[6]-5, y[6]))
ax.annotate(methods[7], (x[7], y[7]), (x[7], y[7]+0.4))
ax.annotate(methods[8], (x[8], y[8]), (x[8]+28, y[8]))
ax.annotate(methods[9], (x[9], y[9]), (x[9], y[9]+0.4))
ax.annotate(methods[10], (x[10], y[10]), (x[10], y[10]+0.4))



plt.scatter(x, y, s=[786.3, 354.3, 752.4, 88.5, 428.7, 311.4, 194.4, 147, 100, 40, 50], c=["g", "b", "g", "b", "r", "r", "r", "b", "g","r", "b" ], marker="1")
plt.xlim(280, -25)
plt.title("Accuracy and params comparison")
plt.xlabel("params (M)")
plt.ylabel("Intersection over Union (%)")
plt.grid(axis='both',linestyle='-.')
plt.show()