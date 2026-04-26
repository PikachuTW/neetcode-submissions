class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        exists = set()
        for num in nums:
            exists.add(num)
        i = 1
        while True:
            if not i in nums:
                return i
            i = i + 1