class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        used = set()
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and ((i, j) not in used):
                    used.add((i ,j))
                    ans += 1
                    arr = [(i, j)]
                    while arr:
                        a, b = arr.pop()
                        
                        for newPos in [(a+1, b), (a-1, b), (a, b+1), (a, b-1)]:
                            if 0 <= newPos[0] <= m-1 and 0 <= newPos[1] <= n-1 and newPos not in used and grid[newPos[0]][newPos[1]] == "1":
                                arr.append(newPos)
                                used.add(newPos)
        return ans
