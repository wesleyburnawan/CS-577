def finishTime(lists):
    return lists[1]

schedule = []
instance = int(input())
for i in range(instance):
    jobs = int(input())
    schedule.append([])
    for j in range(jobs):
        interval = input()
        interval_split = interval.split(' ')
        interval_split[0] = int(interval_split[0])
        interval_split[1] = int(interval_split[1])
        schedule[i].append(interval_split)

print(schedule)

for i in range(instance):
    schedule[i].sort(key=finishTime)
    print(schedule[i])
    output = 1
    index = 1
    finish = schedule[i][0][1]
    while(index < len(schedule[i])):
        if(schedule[i][index][0] >= finish):
            finish = schedule[i][index][1]
            output += 1
        index += 1
    print(output)