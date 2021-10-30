import numpy as np
import matplotlib.pyplot as plt
import cv2


def R5(image):
    """Filtro con Regla 5 para deteccion de fuego"""
    im_read = cv2.imread(image)

    fil, col, ch = im_read.shape

    im_YCbCr = cv2.cvtColor(im_read, cv2.COLOR_RGB2YCrCb)
    # print(im_YCbCr.shape)
    im_filtro = np.zeros((fil, col), dtype=float)

    im_Y = np.zeros((fil, col), dtype=float)
    im_Cb = np.zeros((fil, col), dtype=float)
    im_Cr = np.zeros((fil, col), dtype=float)

    Ysuma = 0
    Cbsuma = 0
    Crsuma = 0
    MxN = fil*col

    
    (im_Y, im_Cb, im_Cr) = cv2.split(im_YCbCr) #, [im_Y, im_Cb, im_Cr]

    # print(im_Y.shape)
    # cv2.imshow("Y channel", im_Y)
    # print(im_Cb.shape)
    # cv2.imshow("Cb channel", im_Cb)
    # print(im_Cr.shape)
    # cv2.imshow("Cr channel", im_Cr)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Promedios de cada canal
    for idx in range(0, fil):
        for idy in range(0, col):
            Ysuma = im_Y[idx][idy] + Ysuma
            Cbsuma = im_Cb[idx][idy] + Cbsuma
            Crsuma = im_Cr[idx][idy] + Crsuma

    Yprom = (Ysuma/MxN)
    Cbprom = (Cbsuma/MxN)
    Crprom = (Crsuma/MxN)

    # Yprom = np.uint8(Yprom)
    # Cbprom = np.uint8(Cbprom)
    # Crprom = np.uint8(Crprom)

    # print(Yprom)
    # print(Cbprom)
    # print(Crprom)
    #Imagen de salidad filtrada
    for idx in range(0, fil):
        for idy in range(0, col):
            if im_Y[idx][idy] >= Yprom and im_Cb[idx][idy] <= Cbprom and im_Cr[idx][idy] >= Crprom:
                im_filtro[idx][idy] = 1
            else:
                im_filtro[idx][idy] = 0

    cv2.imshow("Rule 5", im_filtro)
    cv2.waitKey(0)
    cv2.destroyAllWindows()