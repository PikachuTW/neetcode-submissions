class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        used = set()
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and ((i, j) not in used):
                    ans += 1
                    arr = [(i, j)]
                    while len(arr) > 0:
                        top = arr.pop()
                        if grid[top[0]][top[1]] == "1" and top not in used:
                            used.add(top)
                            if top[0] > 0:
                                arr.append((top[0] - 1, top[1]))
                            if top[0] < m - 1:
                                arr.append((top[0] + 1, top[1]))
                            if top[1] > 0:
                                arr.append((top[0], top[1] - 1))
                            if top[1] < n - 1:
                                arr.append((top[0], top[1] + 1))
        return ans
