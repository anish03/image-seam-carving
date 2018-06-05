import scipy.misc
import numpy as np
import warnings

def cal_energy(image_path):
    warnings.simplefilter("ignore",RuntimeWarning)

    img = scipy.misc.imread(image_path,flatten=False,mode='RGB')
    rows,cols = img.shape[0:2]

    energy_img = np.ndarray(shape=(rows,cols))

    for r in range(0,rows):
        for c in range(0,cols):

            if (c == 0 and r == 0):
                p1 = abs(img[r,c+1][0] - img[r,c][0]) + abs(img[r,c+1][1] - img[r,c][1]) + abs(img[r,c+1][2] - img[r,c][2]) / 3
                p2 = abs(img[r+1,c][0] - img[r,c][0]) + abs(img[r+1,c][1] - img[r,c][1]) + abs(img[r+1,c][2] - img[r+1,c][2]) / 3
                p3 = abs(img[r+1,c+1][0] - img[r,c][0]) + abs(img[r+1,c+1][1] - img[r,c][1]) + abs(img[r+1,c+1][2] - img[r+1,c+1][2]) / 3
                energy_img[r,c] = p1 + p2 + p3
            elif (c == cols - 1 and r == 0):
                p1 = abs(img[r,c-1][0] - img[r,c][0]) + abs(img[r,c-1][1] - img[r,c][1]) + abs(img[r,c-1][2] - img[r,c][2]) / 3
                p2 = abs(img[r-1,c][0] - img[r,c][0]) + abs(img[r-1,c][1] - img[r,c][1]) + abs(img[r-1,c][2] - abs(img[r,c][2])) / 3
                p3 = abs(img[r+1,c-1][0] - img[r,c][0]) + abs(img[r+1,c-1][1] - img[r,c][1]) + abs(img[r+1,c-1][2] - img[r,c][2]) / 3
                energy_img[r,c] = p1 + p2 + p3
            elif (c == 0 and r == rows - 1):
                p1 = abs(img[r-1,c][0] - img[r,c][0]) + abs(img[r-1,c][1] - img[r,c][1]) + abs(img[r-1,c][2] - img[r,c][2]) / 3
                p2 = abs(img[r,c+1][0] - img[r,c][0]) + abs(img[r,c+1][1] - img[r,c][1]) + abs(img[r,c+1][2] - img[r,c][2]) / 3
                p3 = abs(img[r-1,c+1][0] - img[r,c][0]) + abs(img[r-1,c+1][1] - img[r,c][1]) + abs(img[r-1,c+1][2] - img[r,c][2]) / 3
                energy_img[r,c] = p1 + p2 + p3
            elif (c == cols - 1 and r == rows - 1):
                p1 = abs(img[r-1,c-1][0] - img[r,c][0]) + abs(img[r-1,c-1][1] - img[r,c][1]) + abs(img[r-1,c-1][2] - img[r,c][2]) / 3
                p2 = abs(img[r-1,c][0] - img[r,c][0]) + abs(img[r-1,c][1] - img[r,c][1]) + abs(img[r-1,c][2] - img[r,c][2]) / 3
                p3 = abs(img[r,c-1][0] - img[r,c][0]) + abs(img[r,c-1][1] - img[r,c][1]) + abs(img[r,c-1][2] - img[r,c][2]) / 3
                energy_img[r,c] = p1 + p2 + p3
            elif c == 0:
                for i in range(r-1,r+2):
                    for j in range(c,c+2):
                        for rgb in range(0,3):
                            energy_img[r,c] += abs(img[i,j][rgb] - img[r,c][rgb]) / 3
            elif c == cols - 1:
                for i in range(r-1,r+2):
                    for j in range(c-1,c+1):
                        for rgb in range(0,3):
                            energy_img[r,c] += abs(img[i,j][rgb] - img[r,c][rgb]) / 3
            elif r == 0:
                for i in range(r,r+2):
                    for j in range(c-1,c+2):
                        for rgb in range(0,3):
                            energy_img[r,c] += abs(img[i,j][rgb] - img[r,c][rgb]) / 3
            elif r == rows - 1:
                for i in range(r-1,r+1):
                    for j in range(c-1,c+2):
                        for rgb in range(0,3):
                            energy_img[r,c] += abs(img[i,j][rgb] - img[r,c][rgb]) / 3
            else:
                for i in range(r-1,r+2):
                    for j in range(c-1,c+2):
                        for rgb in range(0,3):
                            if i!=r and j!=c:
                                energy_img[r,c] += abs(img[i,j][rgb] - img[r,c][rgb]) / 3

    return energy_img
