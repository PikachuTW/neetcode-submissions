class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        while len(hand) > 0:
            smallest = hand[0]
            hand.remove(smallest)
            for i in range(groupSize - 1):
                if (smallest + i + 1) in hand:
                    hand.remove(smallest + i + 1)
                else:
                    return False

        return True