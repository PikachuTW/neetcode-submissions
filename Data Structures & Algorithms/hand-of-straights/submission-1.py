class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)

        for h in hand:
            start = h
            while count[start-1] > 0:
                start -= 1
            if count[start]:
                for i in range(start, start + groupSize):
                    if count[i] > 0:
                        count[i] -= 1
                    else:
                        return False
            
        return True