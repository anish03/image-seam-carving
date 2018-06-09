import scipy.misc
import numpy as np
import warnings
import math

def cal_energy(image_path):
    warnings.simplefilter("ignore",RuntimeWarning)

    img = scipy.misc.imread(image_path,flatten=False,mode='RGB')
    rows,cols = img.shape[0:2]

    energy_img = np.ndarray(shape=(rows,cols),dtype='int')


    for r in range(0,rows):
        for c in range(0,cols):
            val = 0

            if r == 0 and c == 0:
                for i in range(0,3):
                    val += abs(float(img[r+1,c][i]) - float(img[rows-1,c][i])) ** 2
                    val +=  abs(float(img[r,cols-1][i]) - float(img[r,c+1][i])) ** 2

            elif r == 0 and c == cols - 1:
                for i in range(0,3):
                    val += abs(float(img[r,c-1][i]) - float(img[r,0][i])) ** 2
                    val += abs(float(img[r+1,c][i]) - float(img[rows-1,c][i])) ** 2

            elif r == rows - 1 and c == 0:
                for i in range(0,3):
                    val += abs(float(img[r-1,c][i]) - float(img[0,c][i])) ** 2
                    val += abs(float(img[r,c+1][i]) -  float(img[r,cols-1][i])) ** 2

            elif r == rows - 1 and c == cols - 1:
                for i in range(0,3):
                    val += abs(float(img[r-1,c][i]) - float(img[0,c][i])) ** 2
                    val += abs(float(img[r,c-1][i]) - float(img[r,0][i])) ** 2

            elif c == 0:
                for i in range(0,3):
                    val += abs(float(img[r-1,c][i]) - float(img[r+1,c][i])) ** 2
                    val += abs(float(img[r,c+1][i]) - float(img[r,cols-1][i])) ** 2

            elif c == cols - 1:
                for i in range(0,3):
                    val += abs(float(img[r-1,c][i]) - float(img[r+1,c][i])) ** 2
                    val += abs(float(img[r,c-1][i]) - float(img[r,0][i])) ** 2

            elif r == 0:
                for i in range(0,3):
                    val += abs(float(img[r,c-1][i]) - float(img[r,c+1][i])) ** 2
                    val += abs(float(img[r+1,c][i]) - float(img[rows-1,c][i])) ** 2

            elif r == rows - 1:
                for i in range(0,3):
                    val += abs(float(img[r,c-1][i]) - float(img[r,c+1][i])) ** 2
                    val += abs(float(img[r-1,c][i]) - float(img[0,c][i])) ** 2

            else:
                for i in range(0,3):
                    val += abs(float(img[r,c-1][i]) - float(img[r,c+1][i])) ** 2
                    val += abs(float(img[r-1,c][i]) - float(img[r+1,c][i])) ** 2

            energy_img[r,c] = math.sqrt(val)

    return energy_img
