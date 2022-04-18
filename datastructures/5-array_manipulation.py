# def arrayManipulation(n, queries):
#     # Write your code here
#     # init array of 0 with length of n
#     array = [0]*n
#     for query in queries:
#         start = query[0]
#         end = query[1]

#         value = query[2]
#         for i in range(len(array)):
#             if i >= start-1 and i < end:
#                 if value:
#                     array[i] = array[i] + value
#         print(array)
#     return max(array)

# def arrayManipulation(n, queries):
#     acc = {}
#     for [a, b, k] in queries:
#         acc[a] = (acc[a] if a in acc else 0) + k
#         acc[b+1] = (acc[b+1] if b+1 in acc else 0) - k
#         print(acc)
#     last = 0
#     m = 0
#     for i in range(1, n+1):
#         print("i "+str(i))
#         curr = acc[i] if i in acc else 0
#         print("curr "+str(curr))
#         print("lastbf "+str(last))
#         last = last + curr
#         print("lastaf "+str(last))
#         if (last > m):
#             m = last
#             print("m "+str(m))

#     return m


def arrayManipulation(n, queries):
    arr = [0]*n
    for i in queries:
        arr[i[0] - 1] += i[2]
        if i[1] != len(arr):
            arr[i[1]] -= i[2]
        print(arr)
    maxval = 0
    itt = 0

    for q in arr:
        itt += q
        if itt > maxval:
            maxval = itt
    return maxval


print(arrayManipulation(5, [[1, 2, 3], [2, 4, 5]]))
