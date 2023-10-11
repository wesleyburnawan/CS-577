
class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.vertices = len(graph)

    def BFS(self, source, destination, parent): 
        visited = [False]*(self.vertices)
        queue = []
        queue.append(source)
        visited[source] = True
        while queue:
            u = queue.pop(0)
            for v, w in enumerate(self.graph[u]):
                if visited[v] == False and w > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == destination:
                        return True
        return False

    def FordFulkerson(self, source, sink):
        parent = [-1]*(self.vertices)
        max_flow = 0
        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow +=  path_flow
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow

instance = int(input())
nodeEdge = []
graphs = []

for i in range(instance):
    arr = input()
    arr_split = arr.split(' ')
    for j in range(2):
        arr_split[j] = int(arr_split[j])
    nodeEdge.append(arr_split)
    tempGraph = [[0] * arr_split[0] for _ in range(arr_split[0])]
    for j in range(arr_split[1]):
        #add the edges
        arr = input()
        arr_split = arr.split(' ')
        for k in range(3):
            arr_split[k] = int(arr_split[k])
        tempGraph[arr_split[0]-1][arr_split[1]-1] = arr_split[2] + tempGraph[arr_split[0]-1][arr_split[1]-1]
    graphs.append(Graph(tempGraph))

for i in range(instance):
    print(graphs[i].FordFulkerson(0, nodeEdge[i][0] - 1))