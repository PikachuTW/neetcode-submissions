class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        scope = {}
        i = -1
        for c in s:
            i += 1
            if c in scope:
                scope[c][1] = i
            else:
                scope[c] = [i, i]
        arr = []
        start = 0
        last = 0
        for el in scope:
            if scope[el][0] > last:
                length = last-start+1
                if length != 0:
                    arr.append(length)
                start = scope[el][0]
            last = max(last, scope[el][1])

        length = last-start+1
        if length != 0:
            arr.append(length)
        return arr