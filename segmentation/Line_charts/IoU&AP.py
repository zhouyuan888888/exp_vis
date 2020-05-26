import numpy as np
import matplotlib.pyplot as plt

#1-cascaded
x = np.linspace(0, 1, 5)
y1 = x**3
y2 = x**2

fig,ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(x, y1, color='red', marker="<", label="mIoU")
ax1.legend(loc=2)

ax2.plot(x, y2, color="blue", marker="o", label="PA")
ax2.legend(loc=1)

ax1.set_xlabel('λ')
ax1.set_ylabel('mIoU')
ax2.set_ylabel('PA')


plt.show()