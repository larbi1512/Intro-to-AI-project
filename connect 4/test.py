import numpy as np

good = {
     #"min": 0,
      "max": 1
      }
def count_consecutive_crosses(arr):
        counter = 0
        
        # check right
        i = 0
        while i < len(arr):
            j = 0
            while j < len(arr) - 3:
                if(arr[i][j] in good.values() and arr[i][j+1] in good.values() and arr[i][j+2]
                   in good.values() and arr[i][j+3] in good.values()):
                    counter += 1
                    j += 4
                    while j < len(arr) and arr[i][j] in good.values():
                        counter += 1
                        j += 1
                else:
                    j += 1

            i += 1

        # check down
        j = 0
        while j < len(arr):
            i = 0
            while i < len(arr) - 3:
                if(arr[i][j] in good.values() and arr[i+1][j] in good.values() and arr[i+2][j]
                    in good.values() and arr[i+3][j] in good.values()):
                    counter += 1
                    i += 4
                    while i < len(arr) and arr[i][j] in good.values():
                        counter += 1
                        i += 1
                else:
                    i += 1

            j += 1

        def next_diago_line(i, j):
            if(i > 0):
                i -= 1
                return [i, j]
            
            if(i == 0):
                j += 1
                return [i, j]
            
        # check right-down
        i = len(arr) - 4
        j = 0
        while(j < len(arr) - 3):
            while (i < len(arr) - 3 and i >= j) or (j < len(arr) - 3 and j >= i):
                if(arr[i][j] in good.values() and arr[i+1][j+1] in good.values() and arr[i+2][j+2]
                        in good.values() and arr[i+3][j+3] in good.values()):
                        counter += 1
                        i += 4
                        j += 4
                        while (i < len(arr) and j < len(arr)) and arr[i][j] in good.values():
                            counter += 1
                            i += 1
                            j += 1
                else:
                        i += 1
                        j += 1
                        if(j >= len(arr) - 3 or i >= len(arr) - 3):
                             if i == j:
                                  j = 0; i = 0
                             elif i > j:
                                  i -= j
                                  j = 0
                             elif j > i:
                                  j -= i
                                  i = 0
                             l = next_diago_line(i, j)
                             i = l[0]; j = l[1]

                        

            if i == j:
                j = 0; i = 0
            elif i > j:
                i -= j
                j = 0
            elif j > i:
                j -= i
                i = 0

            l = next_diago_line(i, j)
            i = l[0]; j = l[1]


        # check left-up
        mirror_arr = np.zeros((len(arr), len(arr)))
        for i in range(0, len(arr)):
             for j in range(0, len(arr)):
                  if i + j == len(arr) - 1:
                       mirror_arr[i][j] = 1

        arr = np.dot(arr, mirror_arr)

        i = len(arr) - 4
        j = 0
        while(j < len(arr) - 3):
            while (i < len(arr) - 3 and i >= j) or (j < len(arr) - 3 and j >= i):
                if(arr[i][j] in good.values() and arr[i+1][j+1] in good.values() and arr[i+2][j+2]
                        in good.values() and arr[i+3][j+3] in good.values()):
                        counter += 1
                        i += 4
                        j += 4
                        while (i < len(arr) and j < len(arr)) and arr[i][j] in good.values():
                            counter += 1
                            i += 1
                            j += 1
                else:
                        i += 1
                        j += 1
                        if(j >= len(arr) - 3 or i >= len(arr) - 3):
                             if i == j:
                                  j = 0; i = 0
                             elif i > j:
                                  i -= j
                                  j = 0
                             elif j > i:
                                  j -= i
                                  i = 0
                             l = next_diago_line(i, j)
                             i = l[0]; j = l[1]

                        

            if i == j:
                j = 0; i = 0
            elif i > j:
                i -= j
                j = 0
            elif j > i:
                j -= i
                i = 0

            l = next_diago_line(i, j)
            i = l[0]; j = l[1]

        arr = np.dot(arr, mirror_arr)



        return counter

arr = np.array([[0, 0, 0, 1, 1], 
                [1, 0, 1, 1, 0], 
                [1, 1, 1, 1, 0], 
                [0, 1, 1, 0, 1], 
                [0, 0, 1, 1, 1]])

count = count_consecutive_crosses(arr)

print("Number of four consecutive crosses:", count)


