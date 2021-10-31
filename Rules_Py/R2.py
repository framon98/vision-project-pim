import numpy as np
import matplotlib.pyplot as plt
import cv2

def R2(image):
    """Filtro con Regla 2 para deteccion de fuego"""
    im_read = cv2.imread(image)

    fil, col, ch = im_read.shape

    im_filtro = np.zeros((fil, col), dtype=float)

    for idx in range(0, fil):
        for idy in range(0, col):
            if im_read[idx][idy][0] > 190 and im_read[idx][idy][1] > 100 and im_read[idx][idy][2] < 140:
                im_filtro[idx][idy] = 1
            else:
                im_filtro[idx][idy] = 0
    
    print(fil)
    print(col)
    print(ch)

    
    cv2.imshow("Rule 2", im_filtro)
    cv2.waitKey(0)
    cv2.destroyAllWindows()