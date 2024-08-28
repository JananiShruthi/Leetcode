class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        # Directions for Up, down, left, right
        X = [0,1,0,-1] 
        Y = [-1,0,1,0]
        
        def isValid(x,y,m,n):
            return (x < m and x >= 0 and y < n and y >= 0 and grid[x][y] == "1")

        def dfs(x, y, m, n, grid):
            visited[x][y] = True
            for k in range(4):
                dx = x + X[k]
                dy = y + Y[k]

                if(isValid(dx,dy,m,n) and not visited[dx][dy]):
                    dfs(dx,dy,m,n,grid)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i,j,m,n,grid)
                    ans += 1

        return ans
