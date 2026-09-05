class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            ## check invalid
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] != 1:
                ## return 0 when complete (adding so none is problematio)
                return 0

            ## mark visited
            grid[i][j] = 0

            ## return the area
            return(1 + 
            dfs(i+1, j) +
            dfs(i-1, j) +
            dfs(i, j+1) +
            dfs(i, j-1))
            

        row = len(grid)
        col = len(grid[0])
        max_area = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    ## update for every island
                    max_area = max(max_area, dfs(i, j))

        return max_area