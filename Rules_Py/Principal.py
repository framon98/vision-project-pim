import numpy as np
import matplotlib.pyplot as plt
import cv2
import serial
import time

class Rules:
    def __init__(self, image) -> None:
        print("All")
        self.im_read = cv2.imread(image)

    def serialRead(self):
        ser = serial.Serial('COM7', 9600)
        res = ser.read()
        while True:
            print(res)

    def thermalFilter(self):
        # im_read = cv2.imread(image)

        fil, col, ch = self.im_read.shape

        # im_resized = cv2.resize(im_read, [240, 320])
        im_gray = cv2.cvtColor(self.im_read, cv2.COLOR_BGR2GRAY)

        rid = np.arange(256)
        mid = 225
        sid = np.zeros((256, 1))

        for idx in range(0, 256):
            if rid[idx] >= mid:
                sid[idx] = 255

        im_filtrada = np.zeros((fil, col), np.uint8)

        for idxi in range(0, fil):
            for idxj in range(0, col):
                idxr = im_gray[idxi][idxj]
                idxk = idxr + 1
                if idxk == 256:
                    break
                im_filtrada[idxi][idxj] = sid[idxk]
            
        cv2.imshow("Thermal Image", im_filtrada)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def R1(self, im_read):
        """Filtro con Regla 1 para deteccion de fuego"""
        # im_read = cv2.imread(image)

        fil, col, ch = im_read.shape

        im_filtro = np.zeros((fil, col))

        for idx in range(0, fil):
            for idy in range(0, col):
                if im_read[idx][idy][1] > im_read[idx][idy][2]:
                    if im_read[idx][idy][0] > im_read[idx][idy][1]:
                        im_filtro[idx][idy] = 0
                else:
                    im_filtro[idx][idy] = 1
        return im_filtro
        
    def R2(self, im_read):
        """Filtro con Regla 2 para deteccion de fuego"""
        # im_read = cv2.imread(image)

        fil, col, ch = im_read.shape

        im_filtro = np.zeros((fil, col), dtype=np.double)

        for idx in range(0, fil):
            for idy in range(0, col):
                if im_read[idx][idy][0] > 100 and im_read[idx][idy][1] > 50 and im_read[idx][idy][2] < 100:
                    im_filtro[idx][idy] = 1
                else:
                    im_filtro[idx][idy] = 0

        return im_filtro
        

    def R3(self, im_read):
        """Filtro con Regla 3 para deteccion de fuego"""
        # im_read = cv2.imread(image)

        fil, col, ch = im_read.shape

        im_YCbCr = cv2.cvtColor(im_read, cv2.COLOR_RGB2YCrCb)
        im_filtro = np.zeros((fil, col))

        for idx in range(0, fil):
            for idy in range(0, col):
                if im_YCbCr[idx][idy][0] >= im_YCbCr[idx][idy][1]:
                    im_filtro[idx][idy] = 1
                else:
                    im_filtro[idx][idy] = 0

        return im_filtro

    def R4(self, im_read):
        """Filtro con Regla 3 para deteccion de fuego"""
        # im_read = cv2.imread(image)

        fil, col, ch = im_read.shape

        im_YCbCr = cv2.cvtColor(im_read, cv2.COLOR_RGB2YCrCb)
        im_filtro = np.zeros((fil, col))

        for idx in range(0, fil):
            for idy in range(0, col):
                if im_YCbCr[idx][idy][2] >= im_YCbCr[idx][idy][1]:
                    im_filtro[idx][idy] = 1
                else:
                    im_filtro[idx][idy] = 0
        return im_filtro

    def R5(self, im_read):
        """Filtro con Regla 5 para deteccion de fuego"""
        # im_read = cv2.imread(image)

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
        
        (im_Y, im_Cb, im_Cr) = cv2.split(im_YCbCr)

        # Promedios de cada canal
        for idx in range(0, fil):
            for idy in range(0, col):
                Ysuma = im_Y[idx][idy] + Ysuma
                Cbsuma = im_Cb[idx][idy] + Cbsuma
                Crsuma = im_Cr[idx][idy] + Crsuma

        Yprom = (Ysuma/MxN)
        Cbprom = (Cbsuma/MxN)
        Crprom = (Crsuma/MxN)
        #Imagen de salidad filtrada
        for idx in range(0, fil):
            for idy in range(0, col):
                if im_Y[idx][idy] >= Yprom and im_Cb[idx][idy] <= Cbprom and im_Cr[idx][idy] >= Crprom:
                    im_filtro[idx][idy] = 1
                else:
                    im_filtro[idx][idy] = 0

        return im_filtro

    def R6(self, im_read):
        """Filtro con Regla 6 para deteccion de fuego """
        # im_read = cv2.imread(image)

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
        return im_filtro

    def R7(self, im_read):
        """Filtro con Regla 7 para deteccion de fuego """
        # im_read = cv2.imread(image)

        fil, col, ch = im_read.shape

        im_YCbCr = cv2.cvtColor(im_read, cv2.COLOR_RGB2YCrCb)
        im_filtro = np.zeros((fil, col))

        for idx in range(0, fil):
            for idy in range(0, col):
                if im_YCbCr[idx][idy][1] <= 120 and im_YCbCr[idx][idy][2] >= 150:
                    im_filtro[idx][idy] = 1
                else:
                    im_filtro[idx][idy] = 0
        return im_filtro

    def launch(self):
        # cv2.imshow("Original image", self.im_read)
        Regla_1 = self.R1(self.im_read)
        Regla_2 = self.R2(self.im_read)
        Regla_3 = self.R3(self.im_read)
        Regla_4 = self.R4(self.im_read)
        Regla_5 = self.R5(self.im_read)
        Regla_6 = self.R6(self.im_read)
        Regla_7 = self.R7(self.im_read)

        self.is_fire = 0

        fil, col, ch = self.im_read.shape
        im_7_filtro = np.zeros((fil, col))

        for idx in range(0, fil):
            for idy in range(0, col):
                if Regla_1[idx][idy] == 1 and Regla_3[idx][idy] == 1 and Regla_4[idx][idy] == 1 and Regla_5[idx][idy] == 1 and Regla_6[idx][idy] == 1 and Regla_7[idx][idy] == 1: 
                    # im_7_filtro[idx][idy] = 1
                    self.im_read[idx][idy][0] = 127
                    self.im_read[idx][idy][1] = 0
                    self.im_read[idx][idy][2] = 255
                    self.is_fire += 1
        if self.is_fire > 0:
            print(self.is_fire)
            print("Ther is a Fing Fire!!!")
        cv2.imshow("All rules", self.im_read)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def main():
    root = Rules()
    root.launch()

if __name__ == "__main__":
    main()