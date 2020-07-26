import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import FancyArrowPatch


class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)


params = [ 0.4, 0.61, 0.68, 4.8, 5.8, 7.8, 9, 10.5, 13.5, 26.5, 29.5, 49]
speed = [135.4, 103.7, 81.3,  120, 72.3, 100, 97.5, 57, 22, 30.3, 14.6, 45.7]
accuracy = [58.3, 69.4, 67.3, 67.1, 68.4, 71.3, 74.5, 77.8, 78.9, 69.5, 55.6, 74.7]
label = [ "ENet", "our BCPNet",  "EDANet","DFANet-B", "BiSeNet-1", "DFANet-A", "SFNet-DF1",  "SFNet-DF2", "SFNet-ResNet18", "ICNet", "SegNet", "BiSeNet-2"]
color = ["lime", "blue", "deeppink", "burlywood", "goldenrod", "darkorange", "plum", "darkviolet", "m", "green", "aqua", "brown"]

fig=plt.figure("all")
ax = fig.add_subplot(111,projection='3d')

type0=ax.scatter(params[0], speed[0], accuracy[0], c=color[0], s=10, marker='o')
type1=ax.scatter(params[1], speed[1], accuracy[1], c=color[1], s=40, marker='o')
type2=ax.scatter(params[2], speed[2], accuracy[2], c=color[2], s=80, marker='o')
type3=ax.scatter(params[3], speed[3], accuracy[3], c=color[3], s=120, marker='o')
type4=ax.scatter(params[4], speed[4], accuracy[4], c=color[4], s=160, marker='o')
type5=ax.scatter(params[5], speed[5], accuracy[5], c=color[5], s=200, marker='o')
type6=ax.scatter(params[6], speed[6], accuracy[6], c=color[6], s=240, marker='o')
type7=ax.scatter(params[7], speed[7], accuracy[7], c=color[7], s=280, marker='o')
type8=ax.scatter(params[8], speed[8], accuracy[8], c=color[8], s=320, marker='o')
type9=ax.scatter(params[9], speed[9], accuracy[9], c=color[9], s=360, marker='o')
type10=ax.scatter(params[10], speed[10], accuracy[10], c=color[10], s=400, marker='o')
type11=ax.scatter(params[11], speed[11], accuracy[11], c=color[11], s=440, marker='o')
#type5=ax_all.scatter(params_all[5], speed_all[5], accuracy_all[5], c=color[5], marker='o')
#type6=ax_all.scatter(params_all[6], speed_all[6], accuracy_all[6], c=color[6], marker='o')
#type7=ax_all.scatter(params_all[7], speed_all[7], accuracy_all[7], c=color[7], marker='o')
#type8=ax_all.scatter(params_all[8], speed_all[8], accuracy_all[8], c=color[8], marker='o')

#data annotation
#ax_all.text(params_all[0]-4, speed_all[0]-4, accuracy_all[0]+1, label_all[0], fontsize=7)
ax.text(params[1], speed[1]-4, accuracy[1]+5, label[1], fontsize=12, color="red")
#ax_all.text(params_all[2], speed_all[2]-7, accuracy_all[2]+1.5, label_all[2], fontsize=7)
#ax_all.text(params_all[3], speed_all[3], accuracy_all[3], label_all[3], fontsize=7)
#ax_all.text(params_all[4], speed_all[4], accuracy_all[4], label_all[4], fontsize=7)
#ax_all.text(params_all[5], speed_all[5], accuracy_all[5], label_all[5], fontsize=7)
#ax_all.text(params_all[6], speed_all[6], accuracy_all[6], label_all[6], fontsize=7)
#ax_all.text(params_all[7], speed_all[7], accuracy_all[7], label_all[7], fontsize=7)
#ax_all.text(params_all[8]+1, speed_all[8], accuracy_all[8], label_all[8], fontsize=7)

ax.legend((type0, type1, type2, type3, type4, type5, type6, type7, type8, type9, type10, type11),
                (label[0], label[1], label[2], label[3], label[4], label[5], label[6], label[7], label[8], label[9], label[10], label[11]),
                loc=1,
                bbox_to_anchor=(1.11,1))

arw_BCPNet = Arrow3D([params[1],params[1]],[speed[1]+7, speed[1]],[accuracy[1]+5, accuracy[1]+0.5], arrowstyle="->", color="red", lw = 1.5, mutation_scale=8)
ax.add_artist(arw_BCPNet)

#arw_EDANet = Arrow3D([params_all[2],params_all[2]],[speed_all[2],speed_all[2]],[accuracy_all[2]-0.2, accuracy_all[2]-12.5], arrowstyle="|-|", color="b", lw = 0.5, mutation_scale=2)
#ax_all.add_artist(arw_EDANet)

#arw_DFANet_B = Arrow3D([params_all[3],params_all[3]],[speed_all[3],speed_all[3]],[accuracy_all[3]-0.2, accuracy_all[3]-10], arrowstyle="|-|", color="b", lw = 1, mutation_scale=2)
#ax_all.add_artist(arw_DFANet_B)

#arw_DFANet_A = Arrow3D([params_all[4],params_all[4]],[speed_all[4],speed_all[4]],[accuracy_all[4]-0.2, accuracy_all[4]-14], arrowstyle="|-|", color="b", lw = 1, mutation_scale=2)
#ax_all.add_artist(arw_DFANet_A)

#arw_BiSeNet_1 = Arrow3D([params_all[5],params_all[5]],[speed_all[5],speed_all[5]],[accuracy_all[5]-0.2, accuracy_all[5]-12], arrowstyle="|-|", color="b", lw = 1, mutation_scale=2)
#ax_all.add_artist(arw_BiSeNet_1)

#arw_BiSeNet_2 = Arrow3D([params_all[6],params_all[6]],[speed_all[6],speed_all[6]],[accuracy_all[6]-0.2, accuracy_all[6]-18], arrowstyle="|-|", color="b", lw = 1, mutation_scale=2)
#ax_all.add_artist(arw_BiSeNet_2)

#arw_SegNet = Arrow3D([params_all[7],params_all[7]],[speed_all[7],speed_all[7]],[accuracy_all[7]-0.2, accuracy_all[7]-1.8], arrowstyle="|-|", color="b", lw = 1, mutation_scale=2)
#ax_all.add_artist(arw_SegNet)

#arw_SegNet = Arrow3D([params_all[8],params_all[8]],[speed_all[8],speed_all[8]],[accuracy_all[8]-0.2, accuracy_all[7]-3], arrowstyle="|-|", color="b", lw = 1, mutation_scale=2)
#ax_all.add_artist(arw_SegNet)

ax.set_xlabel("Params (M)")
ax.set_ylabel("Speed (FPS)")
ax.set_zlabel("Accuracy (mIoU)")

plt.draw()
plt.show()
