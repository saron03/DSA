class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def inbound(r, c):
            rows, cols = len(grid), len(grid[0])
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r, c):
            visited[r][c] = True
            directions = [(0,1), (1,0), (-1,0), (0,-1)]

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if inbound(new_r, new_c) and not visited[new_r][new_c] and grid[new_r][new_c] == "1":
                    dfs(new_r, new_c)

        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i, j)
                    island_count += 1

        return island_count
