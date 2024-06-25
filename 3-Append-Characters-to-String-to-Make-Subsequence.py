# question https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/?envType=daily-question&envId=2024-06-03


class Solution(object):
    def appendCharacters(self, s, t):
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1

        return (len(t)) - j
