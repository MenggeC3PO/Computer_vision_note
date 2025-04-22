#!/usr/bin/env python3
"""
Segment an orange cylinder with two colour‑space masks.

    • METHOD A  HSV cuboid     (Hue‑S‑V band)
    • METHOD B  Lab sphere     (perceptual ΔE radius)

Outputs:
    cylinder_mask.png            – final binary mask
    cylinder_preview.png         – original with background blacked out
"""

import cv2
import numpy as np
import sys, os


# ------------------------------------------------------------
# 0. user setting and image loading
# ------------------------------------------------------------
CSV_LOWER = (10, 80, 80)           # HSV lower bound  (H,S,V)
CSV_UPPER = (30, 255, 255)         # HSV upper bound
REF_BGR   = (70, 150, 240)         # reference colour picked on cylinder (B,G,R)
LAB_RAD   = 28                     # Lab‑space radius

img_path = sys.argv[1] if len(sys.argv) > 1 else \
           "/home/cv_user/CV_ws/materials/Color_Thresholding_example.png"
bgr      = cv2.imread(img_path)
if bgr is None:
    raise FileNotFoundError(img_path)

# 1. HSV cuboid mask 
hsv   = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
mask1 = cv2.inRange(hsv, CSV_LOWER, CSV_UPPER)

# 2. Lab sphere mask
ref_bgr = np.uint8([[REF_BGR]])                      
ref_lab = cv2.cvtColor(ref_bgr, cv2.COLOR_BGR2Lab)[0,0].astype(np.int16)
lab_img = cv2.cvtColor(bgr, cv2.COLOR_BGR2Lab).astype(np.int16)
dist2   = np.sum((lab_img - ref_lab)**2, axis=2)
mask2   = (dist2 <= LAB_RAD**2).astype(np.uint8) * 255

# 3. combine & tidy
mask = cv2.bitwise_or(mask1, mask2)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
mask   = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, 2)

cnts,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
if cnts:
    big = max(cnts, key=cv2.contourArea)
    clean = np.zeros_like(mask)
    cv2.drawContours(clean, [big], -1, 255, cv2.FILLED)
    mask = clean

# 4. save & preview 
mask_window   = "binary mask"
result_window = "segmented cylinder"
cv2.imshow(mask_window, mask)  # white = cylinder, black = background

preview = bgr.copy()
preview[mask == 0] = 0
cv2.imshow(result_window, preview)  

# cv2.imwrite("cylinder_mask.png", mask)
# cv2.imwrite("cylinder_preview.png", preview)
cv2.waitKey(0)
cv2.destroyAllWindows()