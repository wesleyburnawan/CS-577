import math

instance = int(input())
data = []
for i in range(instance):
    data.append([])
    num = int(input())
    data[i].append(num)
    arr = input()
    arr_split = arr.split(' ')
    for j in range(data[i][0]):
        arr_split[j] = int(arr_split[j])
    data[i].append(arr_split)

def countSort(array):
    if(len(array) == 1):
        return (array, 0)   
    (arr1, c1) = countSort(array[0: math.ceil(len(array) / 2)])
    (arr2, c2) = countSort(array[math.ceil(len(array)/2) : len(array)])
    (array, c) = mergeCount(arr1, arr2)
    return (array, c + c1 + c2)

def mergeCount(arr1, arr2):
    array = []
    c = 0
    while(len(arr1) > 0 or len(arr2) > 0):
        if(len(arr2) == 0):
            array.append(arr1[0])
            del arr1[0]
        elif(len(arr1) == 0):
            array.append(arr2[0])
            del arr2[0]
            c += len(arr1)
        elif(arr1[0] <= arr2[0]):
            array.append(arr1[0])
            del arr1[0]
        elif(arr1[0] > arr2[0]):
            array.append(arr2[0])
            del arr2[0]
            c += len(arr1)
    return (array, c)

for i in range(instance):
    print(countSort(data[i][1])[1])
