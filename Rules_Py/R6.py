import numpy as np
import matplotlib.pyplot as plt
import cv2

def R6(image):
    """Filtro con Regla 6 para deteccion de fuego """
    im_read = cv2.imread(image)

    fil, col, ch = im_read.shape

    im_YCbCr = cv2.cvtColor(im_read, cv2.COLOR_RGB2YCrCb)
    im_filtro = np.zeros((fil, col))
    im_Y = np.zeros((fil, col), dtype=np.double)
    im_Cb = np.zeros((fil, col), dtype=np.double)
    im_Cr = np.zeros((fil, col), dtype=np.double)

    im_Y, im_Cb, im_Cr = cv2.split(im_YCbCr)

    threshold = 70

    for idx in range(0, fil):
        for idy in range(0, col):
            test = np.double(im_Cb[idx][idy]) - np.double(im_Cr[idx][idy])
            if abs(test) >= threshold:
                im_filtro[idx][idy] = 1
            else:
                im_filtro[idx][idy] = 0

    cv2.imshow("Rule 6", im_filtro)
    cv2.waitKey(0)
    cv2.destroyAllWindows()