import numpy as np
import matplotlib.pyplot as plt
import cv2

def R1(image):
    """Filtro con Regla 1 para deteccion de fuego"""
    im_read = cv2.imread(image)

    fil, col, ch = im_read.shape
    fil = int(fil)
    col = int(col)
    ch = int(ch)

    im_filtro = np.zeros((fil, col))

    for idx in range(0, fil):
        for idy in range(0, col):
            if im_read[idx][idy][1] > im_read[idx][idy][2]:
                if im_read[idx][idy][0] > im_read[idx][idy][1]:
                    im_filtro[idx][idy] = 0
            else:
                im_filtro[idx][idy] = 1
    
    print(fil)
    print(col)
    print(ch)

    # plt.imshow(im_filtro)
    cv2.imshow("Rule 1", im_filtro)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


