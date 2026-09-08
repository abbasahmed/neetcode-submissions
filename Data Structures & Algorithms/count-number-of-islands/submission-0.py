class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        num_islands = 0
        visited = set()
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        if not grid or not grid[0]:
            return 0
        
        def dfs(r, c):
            if (r not in range(rows) or c not in range(cols) or grid[r][c] == '0' or (r, c) in visited):
                return
            visited.add((r,c))
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    num_islands += 1
                    dfs(i, j)

        return num_islands
        
        
