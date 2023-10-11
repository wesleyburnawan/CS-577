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
    cache = []
    page_fault = 0
    index = 0
    while(len(cache) < process[i][0] and index < len(process[i][1])): #fill initial cache
        if(process[i][1][index] not in cache):
            page_fault += 1
            cache.append(process[i][1][index])
        index += 1

    while(index < len(process[i][1])): 
        if(process[i][1][index] not in cache): #if page fault
            page_fault += 1
            cache_future = [] #store future index of call
            for k in cache:
                future = index
                while(future < len(process[i][1]) and k != process[i][1][future]):
                    future += 1
                cache_future.append(future)
            max_index = 0
            max = cache_future[0]
            for n in range(len(cache_future)): #find maximum index in cache_future
                if(cache_future[n] > max):
                    max = cache_future[n]
                    max_index = n
            cache[max_index] = process[i][1][index]  
        index += 1
    print(page_fault)
