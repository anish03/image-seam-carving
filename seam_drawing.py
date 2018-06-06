import numpy as np
import operator
import energy_function_8C as ef
import cv2


def calculateSeam(e):
    m = np.copy(e)
    row_val, col_val = e.shape

    upper_index = np.zeros((row_val, col_val), dtype=int)
    for i in range(1, row_val):
        for j in range(col_val):
            if j == 0:
                flag = 1
                t = (m[i - 1][j], m[i - 1][j + 1])
            elif j == col_val - 1:
                flag = 2
                t = (m[i - 1][j - 1], m[i - 1][j])
            else:
                flag = 3
                t = (m[i - 1][j - 1], m[i - 1][j], m[i - 1][j + 1])

            min_index, min_val = min(enumerate(t), key=operator.itemgetter(1))
            m[i][j] = e[i][j] + min_val
            if flag == 1:
                upper_index[i][j] = min_index
            elif flag == 2 or flag == 3:
                upper_index[i][j] = min_index - 1

    # Backtracking the solution
    min_col_index = min(enumerate(m[row_val - 1]), key=operator.itemgetter(1))[0]

    row, col = row_val - 1, min_col_index
    seam = [(row, col)]
    while row != 0:
        row, col = seam[-1][0], seam[-1][1]
        seam.append((row - 1, col + upper_index[row][col]))
        row -= 1

    return seam


def drawSeam(seam, inp_file, op_file):
    img = cv2.imread(inp_file)
    for i in seam:
        img[i[0], i[1]] = [0, 255, 0]
    cv2.imwrite(op_file, img)


def deleteSeam(seam, inp_file, op_file):
    """
    Partially complete function
    Need some more tuning
    1. Needs shift implementation: Left and right shifting of pixels : In progress
    Current implementation left shift
    :param seam:
    :param inp_file:
    :param op_file:
    :return:
    """
    # d = {x: 1 for x in seam}
    seam = seam[::-1]
    img = cv2.imread(inp_file)
    row_val, col_val, channels = img.shape
    # One less column for seam removal
    blank_image = np.zeros((row_val, col_val - 1, channels), np.uint8)
    for i in range(row_val):
        shift_start = seam[i][1]
        for j in range(shift_start):
            blank_image[i][j] = img[i][j]
        for j in range(shift_start, col_val - 1):
            blank_image[i][j] = img[i][j + 1]

    cv2.imwrite(op_file, blank_image)


def main():
    img = "dolphinstretch2.png"
    e = ef.cal_energy(img)
    s = calculateSeam(e)
    print s
    deleteSeam(s, img, "abc.png")


if __name__ == '__main__':
    main()
