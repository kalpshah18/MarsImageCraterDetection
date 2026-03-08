import cv2
import numpy as np

def adaptive_canny(image):

    gx = cv2.Sobel(image, cv2.CV_64F,1,0)
    gy = cv2.Sobel(image, cv2.CV_64F,0,1)

    mag = np.sqrt(gx**2 + gy**2)

    hist,_ = np.histogram(mag.flatten(), bins=256)

    gm = np.argmax(hist)

    sigma = np.sqrt(np.mean((mag-gm)**2))

    high = gm + sigma
    low = gm * 0.5

    edges = cv2.Canny(image, low, high)

    return edges, gx, gy