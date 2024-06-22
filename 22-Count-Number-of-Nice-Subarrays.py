# question https://leetcode.com/problems/count-number-of-nice-subarrays/description/?envType=daily-question&envId=2024-06-22


class Solution(object):
    def numberOfSubarrays(self, nums, k):
        prevMap = {}
        prevSum = 0
        prevMap[0] = 1
        for elem in nums:
            prevSum += elem % 2
            if prevSum in prevMap:
                prevMap[prevSum] += 1
            else:
                prevMap[prevSum] = 1
        prevSum = 0
        ans = 0
        for elem in nums:
            prevSum += elem % 2
            count = prevSum - k
            if count in prevMap:
                ans += prevMap[count]

        return ans
