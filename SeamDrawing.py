import numpy as np
import operator


def seam_drawing():
    row_val = 5
    col_val = 5
    e = np.random.randint(1, 100, size=(row_val, col_val))
    m = np.copy(e)

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

    print seam


def main():
    seam_drawing()


if __name__ == '__main__':
    main()