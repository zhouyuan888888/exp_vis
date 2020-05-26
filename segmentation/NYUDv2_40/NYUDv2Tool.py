from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
label_colours = [
                (127, 20, 22), (9, 128, 64), (127, 128, 51), (40, 41, 115), (125, 39, 125), (0, 128, 128),
                (127, 127, 127), (57, 16, 18),(191, 32, 38), (65, 128, 61), (191, 128, 43), (67, 41, 122),
                (192, 27, 128), (64, 128, 127),(191, 127, 127), (28, 64, 28),(127, 66, 28), (47, 180, 74),
                (127, 192, 66), (29, 67, 126), (128, 64, 127), (47, 183, 127),(127, 192, 127), (65, 65, 25),
                (191, 67, 38), (75, 183, 73), (190, 192, 49), (64, 64, 127), (193, 65, 128), (74, 187, 127),
                (192, 192, 127), (11, 17, 60),(127, 21, 66),(0, 128, 65), (127, 127, 63), (47, 65, 154),
                (117, 64, 153), (8, 127, 191), (127, 127, 189), (63, 9, 63),(0, 0, 0)]



def decode_labels(mask, num_classes=41):
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
