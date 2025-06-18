class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        status = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append("unvisited")
            status.append(row)
        count = 0

        def inbound(row,col):
            return((0<=row<len(grid)) and (0<=col<len(grid[0])))

        def dfs(row,col):
            status[row][col] = "visited"

            directions = [[0,1],[1,0],[-1,0],[0,-1]]
            for i , j in directions:
                new_row = row + i
                new_col = col + j
                if inbound(new_row,new_col) and grid[new_row][new_col] == "1" and status[new_row][new_col] == "unvisited" :
                    dfs(new_row,new_col)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if status[i][j] == "unvisited" and grid[i][j] == "1":
                    dfs(i,j)
                    count +=1
        return count



