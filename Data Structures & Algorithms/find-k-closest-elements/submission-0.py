class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left = 0
        right = n - 1
        while right - left + 1 > k:
            ld = x - arr[left]
            rd = arr[right] - x
            if rd >= ld:
                right -= 1
            else:
                left += 1
        return arr[left:right+1]