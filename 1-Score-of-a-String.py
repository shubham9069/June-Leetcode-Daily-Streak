# question :-https://leetcode.com/problems/score-of-a-string/description/?envType=daily-question&envId=2024-06-01


class Solution(object):
    def scoreOfString(self, s):
        res = 0

        for i in range(1, len(s)):
            res += abs(ord(s[i - 1]) - ord(s[i]))
        return res
