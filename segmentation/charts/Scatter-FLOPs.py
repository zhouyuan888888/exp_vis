import numpy as np
import matplotlib.pyplot as plt

x = [457.8, 541.4, 412.2, 286, 270, 235, 142.9, 103.8, 64.8, 57.2, 55.3, 28.3, 17.6, 14.8]
y= [63.1 ,73.6 ,81.2 ,57 ,59.8 ,71.8 ,75.2 ,74.2 ,73.2 ,72.9 ,74.7 ,70.6 ,70.7 ,68]
n = np.arange(14)

methods = ["DeepLab", "RefineNet-101", "PSPNet", "SegaNet", "SQ", "FRRN", "CARNet-152", "CARNet-101", "CARNet-50", "TowColumn", "BiseNet2", "ICNet", "CARNet-Mobile", "BiseNet1"]


fig, ax = plt.subplots()

ax.invert_xaxis()#  反转

ax.annotate(methods[0], (x[0], y[0]), (x[0], y[0]+1.3))
ax.annotate(methods[1], (x[1], y[1]), (x[1], y[1]-1.9))
ax.annotate(methods[2], (x[2], y[2]), (x[2], y[2]-1.7))
ax.annotate(methods[3], (x[3], y[3]), (x[3]-20, y[3]))
ax.annotate(methods[4], (x[4], y[4]), (x[4]-20, y[4]))
ax.annotate(methods[5], (x[5], y[5]), (x[5]+80, y[5]))
ax.annotate(methods[6], (x[6], y[6]), (x[6]+130, y[6]))
ax.annotate(methods[7], (x[7], y[7]), (x[7]+130, y[7]-0.6))
ax.annotate(methods[8], (x[8], y[8]), (x[8]+110, y[7]-1.5))
ax.annotate(methods[9], (x[9], y[9]), (x[9]-10, y[9]-0.6))
ax.annotate(methods[10], (x[10], y[10]), (x[10]-10, y[10]+0.6))
ax.annotate(methods[11], (x[11], y[11]), (x[11]+60, y[11]-0.8))
ax.annotate(methods[12], (x[12], y[12]), (x[12]-10, y[12]))
ax.annotate(methods[13], (x[13], y[13]), (x[13]-10, y[13]-0.8))

plt.scatter(x, y, s=[457.8, 541.4, 412.2, 286, 270, 235, 142.9, 123.8, 104.8, 97.2, 95.3, 68.3, 57.6, 54.8], c=["g", "b", "g", "b", "b", "b", "r", "r", "r","b", "b", "g", "r", "b" ], marker="1")
plt.xlim(570, -100)
plt.title("Comparison with other state-of-the-art methods")
plt.xlabel("FLOPs (G)")
plt.ylabel("Intersection over Union (%)")
plt.grid(axis='both',linestyle='-.')
plt.show()
