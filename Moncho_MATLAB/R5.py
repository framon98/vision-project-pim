import numpy as np
import matplotlib.pyplot as plt
import cv2


def R5(image):
    """Filtro con Regla 5 para deteccion de fuego"""
    im_read = cv2.imread(image)

    fil, col, ch = im_read.shape
    fil = int(fil)
    col = int(col)
    ch = int(ch)

    im_YCbCr = cv2.cvtColor(im_read, cv2.COLOR_RGB2YCrCb)
    im_filtro = np.zeros((fil, col))

    im_Y = im_YCbCr[:][:][0]
    im_Cb = im_YCbCr[:][:][1]
    im_Cr = im_YCbCr[:][:][2]