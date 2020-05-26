from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm

labelIds = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
                        #0=unlabeled; 1=ego vehicle; 2=rectification border, 3=out of roi;4=static;
                 (111, 74, 0), (81, 0, 81), (128, 64, 128), (244, 35, 232), (250, 170, 160),
                #5=dynamic;6=ground;7=road;8=sidewalk;9=parking
                 (230, 150, 140), (70, 70, 70), (102, 102, 156), (190, 153, 153), (180, 165, 180),

                 (150, 100, 100), (150, 120, 90), (153, 153, 153), (153, 153, 153), (250, 170, 30),

                 (220, 220, 0), (107, 142, 35), (152, 251, 152), (70, 130, 180), (220, 20, 60),

                 (255, 0, 0), (0, 0, 142), (0, 0, 70), (0, 60, 100), (0, 0, 90),

                 (0, 0, 110), (0, 80, 100), (0, 0, 230), (119, 11, 32), (0, 0, 142)]

labelTrainIds = [(128, 64,128), (244, 35,232),  ( 70, 70, 70), (102,102,156),

                            (190,153,153), (153,153,153), (250,170, 30), (220, 220, 0),

                            (107,142, 35), (152,251,152), ( 70,130,180), (220, 20, 60),

                            (255,  0,  0), (  0,  0,142), (  0,  0, 70), (0, 60, 100),

                            (  0, 80,100), (  0,  0,230), (119, 11, 32)]



def decode_labelIds(mask, num_classes=35):
    """Decode batch of segmentation masks.

    Args:
      mask: result of inference after taking argmax.
      num_images: number of images to decode from the batch.
      num_classes: number of classes to predict (including background).

    Returns:
      A batch with num_images RGB images of the same size as the input.
    """
    h, w = mask.shape
    outputs = np.zeros((h, w, 3), dtype=np.uint8)

    img = Image.new('RGB',(len(mask[0]), len(mask)))
    pixels = img.load()
    for j_, j in enumerate(mask):
        for k_, k in enumerate(j):
            if k < num_classes:
                pixels[k_, j_] = labelIds[k]
    outputs = np.array(img)
    return outputs


def decode_labelTrainIds(mask, num_classes=19):
    """Decode batch of segmentation masks.

    Args:
      mask: result of inference after taking argmax.
      num_images: number of images to decode from the batch.
      num_classes: number of classes to predict (including background).

    Returns:
      A batch with num_images RGB images of the same size as the input.
    """
    h, w = mask.shape
    outputs = np.zeros((h, w, 3), dtype=np.uint8)

    img = Image.new('RGB',(len(mask[0]), len(mask)))
    pixels = img.load()
    for j_, j in enumerate(mask):
        for k_, k in enumerate(j):
            if k < num_classes:
                pixels[k_, j_] = labelTrainIds[k]
    outputs = np.array(img)
    return outputs

if __name__=="__main__":
    data_dir = "E:/日记/light-weight-refinenet改进/cityscapes/results20190623/"
    save_dir = "E:/results20190623RGB/"

    files = os.listdir(data_dir)
    for f in tqdm(files):
        img_p = data_dir + f
        save_p = save_dir + f
        image = np.array(Image.open(img_p))
        image_colour = decode_labelIds(image)
        image_colour = cv2.cvtColor(image_colour, cv2.COLOR_RGB2BGR)# opencv 默认的图片是BGR的格式，所以要进行转换。
        cv2.imwrite(save_p, image_colour)
