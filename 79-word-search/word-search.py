class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(row, col):
            return (0 <= row < rows) and (0 <= col < cols)

        def dfs(r, c,i):
            if i == len(word):
                return True

            if not inbound(r, c) or board[r][c] != word[i]:
                return False
            
            temp = board[r][c]
            board[r][c] = "#"

            for row_change, col_change in directions:
                new_row = r + row_change
                new_col = c + col_change
                if dfs(new_row, new_col,i+1):
                    return True


            board[r][c] = temp  # backtrack
            return False

    
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        return False