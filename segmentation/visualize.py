from cityscapes.CityscapesTool import decode_labelIds
from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt
import cv2


datadir = "E:/日记/light-weight-refinenet改进/VisualizationResults/Cityscapes/mobile/validation/"
savedir =  "E:/日记/light-weight-refinenet改进/VisualizationResults/Cityscapes/mobile/visualization/"

images = os.listdir(datadir)

for file in images:
    img_p = datadir + file
    save_p = savedir + file
    image = np.array(Image.open(img_p))
    image = Image.fromarray(decode_labelIds(image, num_classes=35))
    image.save(save_p)
    print("save {}".format(save_p))






