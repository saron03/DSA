class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        found = False 
        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)

        visited = set()

        def dfs(node,visited):
            nonlocal found
            visited.add(node)
            if node ==destination:
                found = True
                return 
            for n in graph[node]:
                if n not in visited:
                    dfs(n, visited)

        dfs(source, visited)
        return found
            
