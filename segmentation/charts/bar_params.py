import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['CARNet-152', 'CARNet-101', 'CARNet-50', 'CARNet-Mobile']
baseline = [58.1, 42.5, 23.5, 2]#[23.5, 42.5, 58.1, 2.0]
others = [3.6, 3.6, 3.6, 0.5]
CARModule = [0.9, 0.9, 0.9, 0.7]
LCRP = [1, 1, 1, 1]

x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, baseline, width, label='Baseline')
rects2 = ax.bar(x + width/2, others, width, label="Others")
rects3 = ax.bar(x + 3*width/2, LCRP, width, label="LCRP")
rects4 = ax.bar(x + 5*width/2, CARModule, width, label="CARModule")



# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Parameters (M)')
ax.set_title('Parameters comparison of each component')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)

fig.tight_layout()

plt.show()