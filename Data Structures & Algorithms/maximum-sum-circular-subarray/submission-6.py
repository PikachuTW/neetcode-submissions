class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        allNeg = True
        for num in nums:
            if num > 0:
                allNeg = False
        if allNeg:
            return max(nums)
        
        totalSum = sum(nums)

        minSum = 0
        acc = 0
        for num in nums:
            acc += num
            minSum = min(minSum, acc)
            if acc > 0:
                acc = 0

        maxSum = 0
        acc = 0
        for num in nums:
            acc += num
            maxSum = max(maxSum, acc)
            if acc < 0:
                acc =0
        
        return max(maxSum, totalSum - minSum)