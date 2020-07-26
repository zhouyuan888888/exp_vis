from NYUDv2_40.NYUDv2Tool import decode_labels
from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt
import cv2


datadir =  "E:/日记/light-weight-refinenet改进/VisualizationResults/NYUDv2/results/ResNet50/OriginalOutputs/"
savedir =  "E:/日记/light-weight-refinenet改进/VisualizationResults/NYUDv2/results/ResNet50/Visualization/"

images = os.listdir(datadir)

for file in images:
    img_p = datadir + file
    save_p = savedir + file
    image = np.array(Image.open(img_p))
    image = Image.fromarray(decode_labels(image, num_classes=40))
    image.save(save_p)
    print("save {}".format(save_p))
