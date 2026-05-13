class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        gs = 0
        for g in gas:
            gs += g
        cs = 0
        for c in cost:
            cs += c
        if cs > gs:
            return -1
        ans = 0
        cost_sum = 0
        gas_sum = 0
        for i in range(n):
            cost_sum += cost[i]
            gas_sum += gas[i]
            if cost_sum > gas_sum:
                cost_sum = 0
                gas_sum = 0
                ans = i + 1
        return ans