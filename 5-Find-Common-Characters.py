# question https://leetcode.com/problems/find-common-characters/description/?envType=daily-question&envId=2024-06-05



# a little bit optimised methode 
class Solution(object):
    def minWordIndex(self, arr):
        index = 0
        for i in range(1, len(arr)):
            word = arr[i]
            if len(word) < len(arr[index]):
                index = i
        return index

    def commonChars(self, words):
        minIndex = self.minWordIndex(words)
        ans = []
        for ch in words[minIndex]:
            exist = True
            for i in range(0, len(words)):
                if i == minIndex:
                    continue
                if ch not in words[i]:
                    exist = False
                    break
                else:
                    words[i] = words[i].replace(ch, "_", 1)
            if exist:
                ans.append(ch)

        return ans
