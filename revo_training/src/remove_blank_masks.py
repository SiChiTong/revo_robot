import sys, random, os
import cv2

mask_dir = 'data/segmentation/training/masks/msks/'
img_dir = 'data/segmentation/training/images/imgs/'

new_mask_dir = 'data/segmentation_lines/training/masks/msks/'
new_img_dir = 'data/segmentation_lines/training/images/imgs/'

masks = os.listdir(mask_dir)

for m in masks:
    if os.path.getsize(mask_dir + m) > 611:
        msk = cv2.imread(mask_dir + m)
        img = cv2.imread(img_dir + m)
        cv2.imwrite(new_mask_dir + m, msk)
        cv2.imwrite(new_img_dir + m, img)
