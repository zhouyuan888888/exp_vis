from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
label_colours = [(0,0,0)
                # 0=background
                ,(128,0,0),(0,128,0),(128,128,0),(0,0,128),(128,0,128)
                # 1=aeroplane, 2=bicycle, 3=bird, 4=boat, 5=bottle
                ,(0,128,128),(128,128,128),(64,0,0),(192,0,0),(64,128,0)
                # 6=bus, 7=car, 8=cat, 9=chair, 10=cow
                ,(192,128,0),(64,0,128),(192,0,128),(64,128,128),(192,128,128)
                # 11=diningtable, 12=dog, 13=horse, 14=motorbike, 15=person
                ,(0,64,0),(128,64,0),(0,192,0),(128,192,0),(0,64,128)]


def decode_labels(mask, num_classes=21):
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
                pixels[k_, j_] = label_colours[k]
    outputs = np.array(img)
    return outputs

if __name__=="__main__":
    data_dir = "E:/日记/light-weight-refinenet改进/results_encode/"
    save_dir = "E:/ResultsCityscapesRGB/"

    files = os.listdir(data_dir)
    for f in files:
        img_p = data_dir + f
        save_p = save_dir + f
        image = np.array(Image.open(img_p))
        image_colour = decode_labels(image)
        print(img_p)
        cv2.imwrite(save_p, image_colour)
