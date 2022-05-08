def compareTriplets(a, b):
    result = []
    a_point = 0
    b_point = 0
    for i, point in enumerate(a):
        if point > b[i]:
            a_point += 1
        elif point < b[i]:
            b_point += 1
    result.append(a_point)
    result.append(b_point)
    return result


if __name__ == '__main__':
    a = [1, 2, 3]
    b = [3, 2, 1]
    result = compareTriplets(a, b)
    print(result)
