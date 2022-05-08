

def diagonalDifference(arr):
    # Write your code here
    result = 0
    l_to_r_sum = 0
    r_to_l_sum = 0

    left_start_point = 0
    right_start_point = len(ar)-1
    # loop through arr
    for i in range(len(arr)):

        for j in range(len(arr)):
            if (i == j):
                # print(arr[i][j])
                l_to_r_sum += arr[i][j]
                # print(arr[i][right_start_point])
                r_to_l_sum += arr[i][right_start_point]
                right_start_point -= 1
            # print(arr[i][j])

    result = abs(l_to_r_sum - r_to_l_sum)
    return result


if __name__ == '__main__':
    ar = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(diagonalDifference(ar))
