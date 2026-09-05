class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            ## check if valid
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] != "1":
                return

            grid[i][j] = "0"

            ## left
            dfs(i, j-1)
            ## right
            dfs(i, j+1)
            ## down
            dfs(i-1, j)
            ## up
            dfs(i+1, j)
                
        row = len(grid) 
        col = len(grid[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
                    
        return count
    
   