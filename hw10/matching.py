class Graph:
    def __init__(self,graph):
        self.graph = graph
        self.source = len(graph)
        self.destination = len(graph[0])
 
    def dfs(self, source, matching, seen):
        for v in range(self.destination):
            if self.graph[source][v] and seen[v] == False:
                seen[v] = True
                if matching[v] == -1 or self.dfs(matching[v], matching, seen):
                    matching[v] = source
                    return True
        return False
 
    def maxBPM(self):
        matching = [-1] * self.destination
        result = 0

        for i in range(self.source):
            seen = [False] * self.destination
            if self.dfs(i, matching, seen):
                result += 1
        return result

instance = int(input())
nodeEdge = []
graphs = []

for i in range(instance):
    arr = input()
    arr_split = arr.split(' ')
    for j in range(3):
        arr_split[j] = int(arr_split[j])
    nodeEdge.append(arr_split)
    tempGraph = [[0] * arr_split[1] for _ in range(arr_split[0])]
    for j in range(arr_split[2]):
        arr = input()
        arr_split = arr.split(' ')
        for k in range(2):
            arr_split[k] = int(arr_split[k])
        tempGraph[arr_split[0]-1][arr_split[1]-1] = 1
    graphs.append(Graph(tempGraph))

for i in range(instance):
    num = graphs[i].maxBPM()
    if(nodeEdge[i][0] == nodeEdge[i][1]) and (nodeEdge[i][0] == num):
        perfect = 'Y'
    else:
        perfect = 'N'
    print(num, perfect)