class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left = 0
        right = n - k
        while left < right:
            mid = (left + right) // 2
            ld = x - arr[mid]
            rd = arr[mid + k] - x
            if ld > rd:
                left = mid + 1
            else:
                right = mid
        return arr[left:left+k]