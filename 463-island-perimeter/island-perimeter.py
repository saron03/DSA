class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        perimeter= 0
        visited = set()

        def inbound(row,col):
            return (0<=row<len(grid)) and(0<=col<len(grid[0]))
        def dfs(row, col):
            nonlocal perimeter
            if (row, col) in visited:
                return
            visited.add((row, col))
            directions = [[0,-1], [0,1],[1,0], [-1,0]]
            for i, j in directions:
                new_row = row + i
                new_col = col + j
                if not inbound(new_row, new_col) or grid[new_row][new_col] == 0:
                    perimeter += 1
                else:
                    dfs(new_row, new_col)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i,j)
        return perimeter


        
        