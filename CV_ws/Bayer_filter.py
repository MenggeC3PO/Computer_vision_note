""""
Very small Bayer‑filter demo
---------------------------

0. original colour photo
1. raw sensor data (BGGR, grey)
2. colour‑tinted Bayer mosaic (just for visualising the pattern)
3. bilinear demosaicing
4. edge‑aware demosaicing        
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

# ------------------------------------------------------------------
# 0. Load the picture  (pass a path on the command line, or edit here)
# ------------------------------------------------------------------
img_path = sys.argv[1] if len(sys.argv) > 1 else "/home/cv_user/CV_ws/materials/Bayer_filter_example.png"
img_bgr  = cv2.imread(img_path)

if img_bgr is None:
    raise FileNotFoundError(f"Could not read: {img_path}")

img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)   # now in RGB order
h, w = img.shape[:2]

# ------------------------------------------------------------------
# 1. Make a *raw* BGGR frame (one value per pixel)
# ------------------------------------------------------------------
raw = np.zeros((h, w), dtype=img.dtype)
raw[0::2, 0::2] = img[0::2, 0::2, 2]        # B
raw[0::2, 1::2] = img[0::2, 1::2, 1]        # G
raw[1::2, 0::2] = img[1::2, 0::2, 1]        # G
raw[1::2, 1::2] = img[1::2, 1::2, 0]        # R

# ------------------------------------------------------------------
# 2. A colour‑tinted mosaic (just for humans to “see” the pattern)
# ------------------------------------------------------------------
mosaic = np.zeros_like(img)
mosaic[0::2, 0::2, 2] = raw[0::2, 0::2]     # blue dots
mosaic[0::2, 1::2, 1] = raw[0::2, 1::2]     # green dots
mosaic[1::2, 0::2, 1] = raw[1::2, 0::2]     # green dots
mosaic[1::2, 1::2, 0] = raw[1::2, 1::2]     # red dots

# ------------------------------------------------------------------
# 3. Bilinear demosaicing (fast & simple)
# ------------------------------------------------------------------
basic = cv2.cvtColor(raw, cv2.COLOR_BayerBG2BGR)

# ------------------------------------------------------------------
# 4. Edge‑aware demosaicing (sharper; may need OpenCV ≥ 4.5.2)
# ------------------------------------------------------------------
try:
    smart = cv2.cvtColor(raw, cv2.COLOR_BayerBG2BGR_EA)
except cv2.error:
    smart = cv2.cvtColor(raw, cv2.COLOR_BayerBG2BGR_VNG)  # fallback

# 5. Show each stage with OpenCV windows
names  = ["original", "Grey image", "Bayer mosaic", "Basic demosaic", "Advanced demosaic"]
images = [img, raw, mosaic, basic, smart]

for name, im in zip(names, images):
    if im.ndim == 2:                                             # greyscale
        cv2.imshow(name, im)
    else:
        cv2.imshow(name, cv2.cvtColor(im, cv2.COLOR_RGB2BGR))  # back to BGR
cv2.waitKey(0)
cv2.destroyAllWindows()


