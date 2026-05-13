class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ans = 0
        total = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2 or grid[i][j] == 1:
                    total += 1
        while True:
            rottens = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        rottens += 1
            
            if rottens == total:
                return ans
            
            ans += 1

            changed = set()

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        if i > 0 and grid[i-1][j] == 1:
                            changed.add((i-1, j))
                        if i < m - 1 and grid[i+1][j] == 1:
                            changed.add((i+1, j))
                        if j > 0 and grid[i][j-1] == 1:
                            changed.add((i, j-1))
                        if j < n - 1 and grid[i][j+1] == 1:
                            changed.add((i, j+1))

            if len(changed) == 0:
                return -1
            else:
                for c in changed:
                    i, j = c
                    grid[i][j] = 2