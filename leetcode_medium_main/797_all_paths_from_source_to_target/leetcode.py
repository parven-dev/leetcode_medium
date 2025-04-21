

class Solution:
    
    def __init__(self):
        self.graph = []
        
    def add_vertex(self):
        self.graph.append([])
        return len(self.graph)-1 
    
    def add_edge(self, source, destination):
        if destination not in self.graph[source]:
            self.graph[source].append(destination)
        

    def dfs(self):
        # target = len(self.graph)-1
        node = 0
        stack = [(node, [node])]
        result = []
        
        
        while stack:
            (vertex, path) = stack.pop()
            print(vertex, path)
            
            for neighbor in self.graph[vertex]:
                # if neighbor not in path:
                    
                get_path = path + [neighbor]
                if neighbor == len(self.graph) -1:
                    result.append(get_path)
                else:
                    stack.append((neighbor, get_path))
                        
        return result
    
graph = Solution()

# graph_list = [[1,2],[3],[3],[]]
graph_list= [[4,3,1],[3,2,4],[3],[4],[]]

for _ in range(len(graph_list)):
    graph.add_vertex()
    
for u in range(len(graph_list)):
    for v in graph_list[u]:
        graph.add_edge(u, v)

print(graph.dfs())
# print(graph.graph)
