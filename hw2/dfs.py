from collections import defaultdict

class Graph:
    #Constructor
    def __init__(self):
        self.graph = defaultdict(list)

    #function to add edge
    def addEdge(self, s, t):
        self.graph[s].append(t)

    #helper function for dfs
    def dfsHelper(self, s, visited):
        visited.add(s)
        
        if(len(visited) == len(self.graph)):
            print(s,end='\n')
        else:
            print(s,end=' ')
        for neighbor in self.graph[s]:
            if neighbor not in visited and neighbor != '':
                self.dfsHelper(neighbor, visited)
                

    #function to run dfs search
    def dfs(self, s):
        # to store visited nodes
        visited = set()
        for i in range(len(self.graph)): #iterate through dictionary keys
            if list(self.graph)[i] not in visited: #if key not in visited
                self.dfsHelper(list(self.graph)[i], visited)
        

graphs = []
graphs_num = int(input())
for i in range(graphs_num):
    graphs.append(Graph())
    nodes_num = int(input())
    for j in range(nodes_num):
        nodes = input()
        split_nodes = nodes.split(' ')
        if len(split_nodes) > 1:
            for k in range(len(split_nodes) - 1):
                graphs[i].addEdge(split_nodes[0], split_nodes[k+1])
        else:
            graphs[i].addEdge(split_nodes[0], '')

for i in range(graphs_num):
    graphs[i].dfs(list(graphs[i].graph)[0])
