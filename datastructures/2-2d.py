m = None


def hourglassSum(arr):
    # Write your code here
    max = None
    for x in range(1, 5):
        for y in range(1, 5):
            # print(arr[x][y])
            core = arr[x][y]
            topleft = arr[x-1][y-1]
            # top mid  -1 0
            topmid = arr[x-1][y]
            # top right -1 +1
            topright = arr[x-1][y+1]
            # lower left +1 -1
            lowleft = arr[x+1][y-1]
            # lower mid +1 0
            lowmid = arr[x+1][y]
            # lower right +1 +1
            lowright = arr[x+1][y+1]
            # hourglass sum
            hourglass_sum = core+topleft+topmid+topright+lowleft+lowmid+lowright
            if max == None or max < hourglass_sum:
                max = hourglass_sum
    return max


def rotateLeft(d, arr):
    # Write your code here
    slice = arr[:d]
    otherslice = arr[d:]
    return otherslice + slice


arr = [1, 2, 3, 4]
rotateLeft(2, arr)
