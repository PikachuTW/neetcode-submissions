class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        used = [[False for _ in range(n)] for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not used[i][j]:
                    used[i][j] = True
                    ans += 1
                    arr = [(i, j)]
                    while arr:
                        a, b = arr.pop()
                        
                        for newPos in [(a+1, b), (a-1, b), (a, b+1), (a, b-1)]:
                            c, d = newPos
                            if 0 <= c <= m-1 and 0 <= d <= n-1 and not used[c][d] and grid[c][d] == "1":
                                arr.append(newPos)
                                used[c][d] = True
        return ans
