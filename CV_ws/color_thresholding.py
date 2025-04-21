#!/usr/bin/env python3
"""
Colour‑threshold demo on berries.png
------------------------------------
• CUBOID  (RGB axis‑aligned)  → catches every raspberry, leaks background
• SPHERE  (Lab Euclidean)     → isolates the single blackberry
"""

import cv2
import numpy as np
import sys, os

# ----------------------------------------------------------------------
# 0. read the image you provided
# ----------------------------------------------------------------------
img_path = sys.argv[1] if len(sys.argv) > 1 else \
           "/home/cv_user/CV_ws/materials/Color_Thresholding_example.png"
img_bgr  = cv2.imread(img_path)
if img_bgr is None:
    raise FileNotFoundError(img_path)

# ----------------------------------------------------------------------
# 1. hard‑coded reference colours  (picked from the picture)
# ----------------------------------------------------------------------
# raspberry red  (RGB)  &  cuboid half‑sizes
target_rgb_rasp = np.array([200,  60, 105], dtype=np.uint8)   # (R,G,B)
dR, dG, dB      = 80, 80, 80                                  # generous box

# blackberry dark purple (RGB)  &  Lab‑sphere radius
target_rgb_blk  = np.array([ 40,  30,  60], dtype=np.uint8)   # (R,G,B)
R_lab           = 35                                          # Lab units

# ----------------------------------------------------------------------
# 2. build *CUBOID* mask   (RGB box around raspberries)
# ----------------------------------------------------------------------
lower_rgb = np.clip(target_rgb_rasp - (dR, dG, dB), 0, 255)
upper_rgb = np.clip(target_rgb_rasp + (dR, dG, dB), 0, 255)
mask_cub  = cv2.inRange(img_bgr, lower_rgb, upper_rgb)        # 0/255

# ----------------------------------------------------------------------
# 3. build *SPHERE* mask   (Lab distance from blackberry colour)
# ----------------------------------------------------------------------
lab       = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2Lab).astype(np.int16)
target_lab = cv2.cvtColor(target_rgb_blk.reshape(1,1,3), cv2.COLOR_BGR2Lab)\
                .astype(np.int16).reshape(3)

dist2     = np.sum((lab - target_lab)**2, axis=2)
mask_sph  = (dist2 <= R_lab**2).astype(np.uint8) * 255

# ----------------------------------------------------------------------
# 4. helper to overlay a mask on the original image
# ----------------------------------------------------------------------
def overlay(src, mask, colour=(255,255,255), alpha=0.55):
    out = src.copy()
    sel = mask.astype(bool)
    if sel.any():                                              # avoid empty slice
        out[sel] = cv2.addWeighted(src[sel], 1-alpha,
                                   np.full_like(src[sel], colour), alpha, 0)
    return out

ov_cub = overlay(img_bgr, mask_cub)             # raspberries (box)
ov_sph = overlay(img_bgr, mask_sph)             # blackberry  (sphere)

# ----------------------------------------------------------------------
# 5. show results
# ----------------------------------------------------------------------
cv2.imshow("original",          img_bgr)
cv2.imshow("CUBOID raspberries (leaks)", ov_cub)
cv2.imshow("SPHERE blackberry  (tight)", ov_sph)

print("--- pixel counts ----------------------------------------")
print("cuboid mask :", np.count_nonzero(mask_cub))
print("sphere mask :", np.count_nonzero(mask_sph))
print("Close a window or hit any key in one of them to exit.")
cv2.waitKey(0)
cv2.destroyAllWindows()
