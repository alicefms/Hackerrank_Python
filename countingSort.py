def countingSort(arr):
    arr2 = []
    arr.sort()

    for e in range(0, arr[len(arr) -1] +1):
        arr2.append(0)

    for e in arr:
        arr2[e] = arr2[e] + 1
    return arr2


print(countingSort([1,1,3,2,1]))