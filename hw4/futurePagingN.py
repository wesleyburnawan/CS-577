process = []
dict_request = [] #store each unique page request and the index of each request
instance = int(input())
for i in range(instance):
    dict_request.append({})
    process.append([])
    page = int(input())
    process[i].append(page)
    request = int(input())
    call = input()
    call_split = call.split(' ')
    if(len(call_split[len(call_split) - 1]) == 0):
        del call_split[len(call_split) - 1]
    for j in range(request):
        call_split[j] = int(call_split[j])
    process[i].append(call_split)
    for k in range(request):
        if(process[i][1][k] in dict_request[i]):
            dict_request[i][process[i][1][k]].append(k)
        else:
            dict_request[i].update({process[i][1][k]:[k]})

for i in range(instance):
    cache = {} #store cache in the form of page as key and future key access as value
    page_fault = 0
    index = 0
    # fill cache until full
    while(index < len(process[i][1]) and len(cache) < process[i][0]):
        if(process[i][1][index] not in cache):
            page_fault += 1
            if(len(dict_request[i][process[i][1][index]]) < 2):
                cache.update({process[i][1][index]:len(process[i][1])})
            else:
                cache.update({process[i][1][index]:dict_request[i][process[i][1][index]][1]})
        else:
            if(len(dict_request[i][process[i][1][index]]) < 2):
                cache[process[i][1][index]] = len(process[i][1])
            else:
                cache[process[i][1][index]] = dict_request[i][process[i][1][index]][1]
        del dict_request[i][process[i][1][index]][0]

        index += 1

    # After cache is full
    while(index < len(process[i][1])):
        if(process[i][1][index] not in cache):
            page_fault += 1
            val_list = cache.values()
            max_val = max(val_list)
            max_index = list(cache.values()).index(max_val)
            max_key = list(cache.keys())[max_index]
            cache.pop(max_key)
            if(len(dict_request[i][process[i][1][index]]) < 2):
                cache.update({process[i][1][index]:len(process[i][1])})
            else:
                cache.update({process[i][1][index]:dict_request[i][process[i][1][index]][1]})
        else:
            if(len(dict_request[i][process[i][1][index]]) < 2):
                cache[process[i][1][index]] = len(process[i][1])
            else:
                cache[process[i][1][index]] = dict_request[i][process[i][1][index]][1]
        del dict_request[i][process[i][1][index]][0]
        index += 1
    print(page_fault)