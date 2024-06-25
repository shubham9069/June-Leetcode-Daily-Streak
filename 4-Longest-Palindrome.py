# https://leetcode.com/problems/longest-palindrome/description/?envType=daily-question&envId=2024-06-04


class Solution(object):
    def longestPalindrome(self, s):
        res = 0
        val = False
        mp = {}

        for ch in s:
            mp[ch] = mp.get(ch, 0) + 1
        for count in mp.values():
            if count % 2 != 0:
                res += count - 1
                val = True
            else:
                res += count
        if val:
            res = res + 1
        return res
