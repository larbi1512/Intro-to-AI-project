import numpy as np

def next_move(i, j, size):
    if i >= size - j - 1 and i < j:
        i += 1
    elif j > size - i - 1 and j <= i:
        j -= 1
    elif i >= j and j <= size - i - 1:
        i -= 1
    else:
        j += 1

    return [i, j]

arr = np.array([[25, 10, 11, 12, 13],
                [24, 9, 2, 3, 14],
                [23, 8, 1, 4, 15],
                [22, 7, 6, 5, 16],
                [21, 20, 19, 18, 17]])


i = int(np.floor(5 / 2) - (not 5 % 2))
j = int(np.floor(5 / 2) - (not 5 % 2) + (5 + 1) % 2)
while i != -1:
    print(arr[i][j])

    l = next_move(i, j, 5)
    i = l[0]; j = l[1]

