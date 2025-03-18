 
class Solution:
 
    def __init__(self):
            self.graph = []
        
    def add_vertex(self):
        self.graph.append([])
        return len(self.graph)-1 
    
    def add_edge(self, source, destination):
        if destination not in self.graph[source]:
            self.graph[source].append(destination)
        
    def findSmallestSetOfVertices(self, n):
        
        incoming_edge = [0] * n
        anser = []

            
        for from_node , to_node in edges:
            incoming_edge[to_node] += 1
        
        
        for i in range(5):
            if incoming_edge[i] == 0:
                anser.append(i)
                
        return  anser


graphs = Solution()

# graph_list = [[1,2],[3],[3],[]]
edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
n = 6

for _ in range(len(edges)):
    graphs.add_vertex()
    
for u in range(len(edges)):
    for v in edges[u]:
        graphs.add_edge(u, v)
        

print(graphs.findSmallestSetOfVertices(n))
        
# print(graphs.graph)
