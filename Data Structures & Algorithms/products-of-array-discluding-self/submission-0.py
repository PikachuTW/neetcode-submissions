class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]
        for i in range(n):
            prefix.append(prefix[i] * nums[i])
        suffix = [1]
        for i in range(n):
            suffix.append(suffix[i] * nums[n - i - 1])
        ans = []
        for i in range(n):
            ans.append(prefix[i] * suffix[n - i - 1])
        return ans