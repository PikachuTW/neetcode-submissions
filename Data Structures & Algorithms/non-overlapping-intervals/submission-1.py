class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        last = -100000
        count = 0
        for interval in intervals:
            if interval[0] < last:
                last = min(last, interval[1])
                count += 1
            else:
                last = interval[1]
        return count