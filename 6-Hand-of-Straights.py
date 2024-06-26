# question https://leetcode.com/problems/hand-of-straights/submissions/1301089564/?envType=daily-question&envId=2024-06-06


class Solution:

    def find_successors(self, hand: List[int], groupSize: int, i: int, n: int):
        next_val = hand[i] + 1
        hand[i] = -1
        count = 1
        i += 1
        while i < n and count < groupSize:
            if hand[i] == next_val:
                next_val = hand[i] + 1
                hand[i] = -1
                count += 1
            i += 1
        return count == groupSize

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        hand.sort()
        for i in range(n):
            if hand[i] >= 0:
                if not self.find_successors(hand, groupSize, i, n):
                    return False
        return True
