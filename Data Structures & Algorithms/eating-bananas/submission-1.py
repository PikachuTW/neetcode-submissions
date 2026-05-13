class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l < r:
            mid = (l + r) // 2
            expected_time = 0
            for pile in piles:
                expected_time += math.ceil(pile / mid)
            if expected_time > h:
                l = mid + 1
            else:
                r = mid
        return l