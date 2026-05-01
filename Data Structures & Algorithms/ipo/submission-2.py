class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        arr = []
        heap = []
        for i in range(n):
            arr.append((capital[i], profits[i]))
        arr.sort()
        ai = 0
        for i in range(k):
            while ai < n and arr[ai][0] <= w:
                heapq.heappush(heap, -arr[ai][1])
                ai += 1
            if len(heap) > 0:
                most = -heapq.heappop(heap)
            else:
                return w
            w += most
        return w


        