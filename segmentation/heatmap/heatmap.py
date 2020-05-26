import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import axes
from PIL import Image


def draw_heatmap(image_path,save_path):
    # cmap=cm.Blues
    data= np.array(Image.open(image_path))
    cmap = cm.get_cmap('rainbow', 1000)
    figure = plt.figure(facecolor='w')
    ax = figure.add_subplot(1, 1, 1, position=[0.1, 0.15, 0.8, 0.8])
    #ax.set_yticks(range(len(ylabels)))
    #ax.set_yticklabels(ylabels)
    #ax.set_xticks(range(len(xlabels)))
    #ax.set_xticklabels(xlabels)
    vmax = 0
    vmin = 255
    for i in data:
        for j in i:
            if j > vmax:
                vmax = j
            if j < vmin:
                vmin = j
    map = ax.imshow(data, interpolation='bilinear', cmap=cmap, aspect='auto', vmin=vmin, vmax=vmax)
    cb = plt.colorbar(mappable=map, cax=None, ax=None, shrink=0.5)
    plt.savefig("/home/zhouyuan/cabnet/test/nyud/scloss/000976.png")
    print("saving:"+save_path)