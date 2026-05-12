class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        validNum = set()
        for i in range(1, 26 + 1):
            validNum.add(str(i))

        dp[0] = 1

        for i in range(1, n + 1):
            lastNumOne = s[i-1]
            lastNumTwo = s[i-2] + s[i-1]
            if i >= 1 and lastNumOne in validNum:
                dp[i] += dp[i-1]
            if i >= 2 and lastNumTwo in validNum:
                dp[i] += dp[i-2]
        return dp[n]