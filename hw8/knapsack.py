instance = int(input())
data_capacity = []
data_list = []

for i in range(instance):
    arr = input()
    arr_split = arr.split(' ')
    for j in range(2):
        arr_split[j] = int(arr_split[j])
    data_capacity.append(arr_split)
    data_list.append([])
    for k in range(data_capacity[i][0]):
        arr = input()
        arr_split = arr.split(' ')
        for j in range(2):
            arr_split[j] = int(arr_split[j])
        data_list[i].append(arr_split)

for i in range(instance):
    solution = [[0 for x in range(data_capacity[i][1] + 1)] for x in range(data_capacity[i][0] + 1)]
    for j in range(data_capacity[i][0] + 1):
        for w in range(data_capacity[i][1] + 1):
            if j == 0 or w == 0:
                solution[j][w] = 0
            elif data_list[i][j-1][0] <= w:
                solution[j][w] = max(data_list[i][j-1][1] + solution[j-1][w-data_list[i][j-1][0]], solution[j-1][w])
            else:
                solution[j][w] = solution[j-1][w]
    print(solution[data_capacity[i][0]][data_capacity[i][1]])