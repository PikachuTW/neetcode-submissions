class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        rq = deque()
        dq = deque()
        for i in range(n):
            if senate[i] == "R":
                rq.append(i)
            else:
                dq.append(i)
        while True:
            if len(dq) == 0:
                return "Radiant"
            elif len(rq) == 0:
                return "Dire"
            rl = rq.popleft()
            dl = dq.popleft()
            if rl < dl:
                rq.append(rl + n)
            else:
                dq.append(dl + n)
            