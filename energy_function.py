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

            if c == cols-1:
                C = 0
            else:
                C = c + 1

            R_x = abs(img[r,c-1][0] - img[r,C][0])
            G_x = abs(img[r,c-1][1] - img[r,C][1])
            B_x = abs(img[r,c-1][2] - img[r,C][2])
            del_x = (R_x**2) + (G_x**2) + (B_x**2)

            if r == rows-1:
                R = 0
            else:
                R = r + 1

            R_y = abs(img[r-1,c][0] - img[R,c][0])
            G_y = abs(img[r-1,c][1] - img[R,c][1])
            B_y = abs(img[r-1,c][2] - img[R,c][2])
            del_y = (R_y**2) + (G_y**2) + (B_y**2)

            energy_img[r,c] = del_x + del_y

    return energy_img
