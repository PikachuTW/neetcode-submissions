class Solution:

    def openLock(self, deadends: List[str], target: str) -> int:
        occured = set("0000")
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        q = collections.deque([("0000", 0)])
        while q:
            s, depth = q.popleft()

            if s == target:
                return depth

            for i in range(4):
                for k in [1, -1]:
                    newDigit = (int(s[i]) + k) % 10
                    nextState = s[:i] + str(newDigit) + s[i+1:]
                    if nextState in occured or nextState in deadends:
                        continue
                    q.append((nextState, depth+1))
                    occured.add(nextState)

        return -1
