import numpy as np
import matplotlib.pyplot as plt

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n".format(pct)

#50
recipe50 = ["23.508 M Baseline", "3.557 M Others", "0.9427 M CARModule", "1.0486 M LCRP"]
#101
recipe101 = ["42.5001 M Baseline", "3.5571 M Others", "0.9418 M CARModule", "1.0494 M LCRP"]

#152
recipe152 = ["58.1438 M Baseline", "3.557 M Others", "0.9427 M CARModule", "1.0486 M LCRP"]

#Mobile
recipemobile = ["1.991 M Baseline", "0.5423 M Others", "0.707 M CARModule", "1.0486 M LCRP"]


fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))


data50 = [float(x.split()[0]) for x in recipe152]
ingredients = [x.split()[-1] for x in recipe152]

wedges50, texts50, autotexts50 = ax.pie(data50, autopct=lambda pct: func(pct, data50), textprops=dict(color="black"), explode=[0, 0, 0, 0], radius=1.3)


ax.legend(wedges50, ingredients, title="Components", loc="upper left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.setp(autotexts50, size=10)


ax.set_title("CARNet-152")

plt.show()