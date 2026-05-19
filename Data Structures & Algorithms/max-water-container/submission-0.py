class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                ans = max(ans, min(heights[i], heights[j]) * (j-i))
        return ans