import numpy as np
import matplotlib.pyplot as plt



N = 7
baseline = (58.1, 42.5, 23.5, 58.1, 42.5, 23.5, 3.3)
Refine = (75.6, 75.6, 75.6, 5.2, 5.2, 5.2, 0.6)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, baseline, width)
p2 = plt.bar(ind, Refine, width,
             bottom=baseline)

plt.ylabel('Parameters (M)')
plt.title('Parameters comparison')
plt.xticks(ind, ('RF-152', 'RF-101', 'RF-50', 'ours-152', 'ours-101', 'ours-50', 'ours-Mobile'))
plt.yticks(np.arange(0, 140, 40))
plt.legend((p1[0], p2[0]), ('baseline', 'refinement pipeline'))
plt.xticks(rotation=10)

plt.show()