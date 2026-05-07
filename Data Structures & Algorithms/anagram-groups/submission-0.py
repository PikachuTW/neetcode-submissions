class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        sorted_strs = []
        for s in strs:
            sorted_s = []
            for c in s:
                sorted_s.append(c)
            sorted_s.sort()
            sorted_str = ""
            for c in sorted_s:
                sorted_str += c
            sorted_strs.append(sorted_str)
        
        mm = {}
        for i in range(n):
            if sorted_strs[i] in mm:
                mm[sorted_strs[i]].append(strs[i])
            else:
                mm[sorted_strs[i]] = [strs[i]]
        ans = []
        for m in mm:
            ans.append(mm[m])
        return ans