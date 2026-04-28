class Solution:
    def next_state(self, s: str, digit: int, inc: int) -> str:
        num = int(s)
        c = int(s[3 - digit])
        nc = (c + inc) % 10
        num -= c * (10 ** digit)
        num += nc * (10 ** digit)
        ans = str(num)
        while len(ans) < 4:
            ans = "0" + ans
        return ans

    def openLock(self, deadends: List[str], target: str) -> int:
        occured = set()
        deadends = set(deadends)
        q = collections.deque([("0000", 0)])
        while len(q) != 0:
            s, depth = q.popleft()

            if s in occured or s in deadends:
                continue

            occured.add(s)

            if s == target:
                return depth

            for i in range(4):
                q.append((self.next_state(s, i, 1), depth + 1))
                q.append((self.next_state(s, i, -1), depth + 1))

        return -1
