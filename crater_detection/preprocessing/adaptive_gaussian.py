import cv2
import numpy as np

def local_std(img, k=3):
    mean = cv2.blur(img, (k, k))
    sq_mean = cv2.blur(img**2, (k, k))
    return np.sqrt(sq_mean - mean**2)

def multi_scale_adaptive_gaussian(image):
    img = image.astype(np.float32)

    lsd = local_std(img, 5)

    hist = np.histogram(lsd, bins=256)
    gamma_m = hist[1][np.argmax(hist[0])]

    edge_region = lsd > gamma_m
    non_edge_region = lsd <= gamma_m

    smooth1 = cv2.GaussianBlur(img, (3,3), 0.5)
    smooth2 = cv2.GaussianBlur(img, (7,7), 1.5)

    result = img.copy()
    result[edge_region] = smooth1[edge_region]
    result[non_edge_region] = smooth2[non_edge_region]

    return result.astype(np.uint8)