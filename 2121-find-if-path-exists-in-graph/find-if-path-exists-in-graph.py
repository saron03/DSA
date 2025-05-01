class Solution(object):
    from collections import defaultdict
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        dic1= defaultdict(list)
        for i in edges:
            dic1[i[0]].append(i[1])
            dic1[i[1]].append(i[0])
        visited = set()
        def dfs(node):
            if node == destination:
                return True
            visited.add(node)
            for i in dic1[node]:
                if i not in visited:
                    found = dfs(i)
                    if found:
                        return True
            return False
        return dfs(source)