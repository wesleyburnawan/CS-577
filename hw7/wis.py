import math 

instance = int(input())
data = []
schedule = []
optimal = []
for i in range(instance):
    schedule.append([])
    num = int(input())
    data.append(num)
    for j in range(num):
        arr = input()
        arr_split = arr.split(' ')
        for k in range(3):
            arr_split[k] = int(arr_split[k])
        schedule[i].append(arr_split)
    schedule[i].sort(key=lambda x:x[1])

for i in range(instance):
    optimal.append(schedule[i][0][2]) #get first schedule weight
    for j in range(1, data[i]):
        #get previous compatible schedule
        k = j - 1
        while(k >= 0):
            if (schedule[i][j][0] >= schedule[i][k][1]):
                break
            k -= 1 
        if(k < 0):
            optimal.append(max(optimal[j-1], schedule[i][j][2]))
        else:
            optimal.append(max(optimal[j-1], optimal[k] + schedule[i][j][2]))
    print(optimal[data[i]-1])
    optimal = []