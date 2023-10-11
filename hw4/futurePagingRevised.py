process = []
instance = int(input())
for i in range(instance):
    process.append([])
    page = int(input())
    process[i].append(page)
    request = int(input())
    call = input()
    call_split = call.split(' ')
    for j in range(request):
        call_split[j] = int(call_split[j])
    process[i].append(call_split)

for i in range(instance):
    cache = {}
    page_fault = 0
    index = 0
    while(len(cache) < process[i][0] and index < len(process[i][1])): #fill initial cache
        future = index
        if(future < len(process[i][1]) - 1):
            future += 1
            while(future < len(process[i][1]) and process[i][1][index] != process[i][1][future]):
                future += 1
        if(process[i][1][index] not in cache):
            page_fault += 1
            cache.update({process[i][1][index]:future})
        else:
            cache[process[i][1][index]] = future
        index += 1
    
    # After cache is full
    while(index < len(process[i][1])):
        future = index
        if(future < len(process[i][1]) - 1):
            future += 1
            while(future < len(process[i][1]) and process[i][1][index] != process[i][1][future]):
                future += 1
        if(process[i][1][index] not in cache): #if page fault
            page_fault += 1
            val_list = cache.values()
            max_value = max(val_list)
            max_index = list(cache.values()).index(max_value)
            max_key = list(cache.keys())[max_index]
            cache.pop(max_key)
            cache.update({process[i][1][index]:future})
        else:
            cache[process[i][1][index]] = future
        index += 1
    print(page_fault)
