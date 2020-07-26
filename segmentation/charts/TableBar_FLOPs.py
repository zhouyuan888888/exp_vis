import numpy as np
import matplotlib.pyplot as plt

N = 7
baseline = (70.6, 47.8, 24.9, 70.6, 47.8, 24.9, 9.1)
Refine = (260.3, 260.3, 260.3, 13.2, 13.2, 13.2, 1.9)
ind = np.arange(N)    # the x locations for the groups
width = 0.4       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, baseline, width)
p2 = plt.bar(ind, Refine, width,
             bottom=baseline)

plt.ylabel('FLOPs (G)')
plt.title('FLOPs comparison')
plt.xticks(ind, ('RF-152', 'RF-101', 'RF-50', 'ours-152', 'ours-101', 'ours-50', 'ours-Mobile'))
plt.yticks(np.arange(0, 360, 50))
plt.legend((p1[0], p2[0]), ('baseline', 'refinement pipeline'))
plt.xticks(rotation=10)

plt.show()