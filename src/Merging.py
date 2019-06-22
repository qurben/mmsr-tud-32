import sys
import cv2

from scene_change import merge, add_noise, add_blur
from vanishing_point import resize_image

foregroundPath = sys.argv[1]
backgroundPath = sys.argv[2]

foreground = resize_image(cv2.imread(foregroundPath, cv2.IMREAD_UNCHANGED), 512)
background = resize_image(cv2.imread(backgroundPath), 512)

merged = merge(foreground, background)
cv2.imshow('Merged', merged)
cv2.waitKey(0)

blurred = add_blur(merged, 3)
cv2.imshow('Blurred', blurred)
cv2.waitKey(0)

noisy = add_noise(blurred)
cv2.imshow('Noisy', noisy)
cv2.waitKey(0)