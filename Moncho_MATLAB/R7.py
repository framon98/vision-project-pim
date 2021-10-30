import numpy as np
import matplotlib.pyplot as plt
import cv2

def R7(image):
    """Filtro con Regla 7 para deteccion de fuego """
    im_read = cv2.imread(image)

    fil, col, ch = im_read.shape

    im_YCbCr = cv2.cvtColor(im_read, cv2.COLOR_RGB2YCrCb)
    im_filtro = np.zeros((fil, col))

    for idx in range(0, fil):
        for idy in range(0, col):
            if im_YCbCr[idx][idy][1] <= 120 and im_YCbCr[idx][idy][2] >= 150:
                im_filtro[idx][idy] = 1
            else:
                im_filtro[idx][idy] = 0

    cv2.imshow("Rule 7", im_filtro)
    cv2.waitKey(0)
    cv2.destroyAllWindows()