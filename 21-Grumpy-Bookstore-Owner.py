# question https://leetcode.com/problems/grumpy-bookstore-owner/description/?envType=daily-question&envId=2024-06-21


class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        n = len(customers)
        custUnSatisfy = 0
        maxUnSatisfy = 0

        for i in range(0, minutes):
            custUnSatisfy += customers[i] * grumpy[i]
        maxUnSatisfy = custUnSatisfy
        i = 0
        j = minutes

        while j < n:
            custUnSatisfy += customers[j] * grumpy[j]
            custUnSatisfy -= customers[i] * grumpy[i]
            maxUnSatisfy = max(maxUnSatisfy, custUnSatisfy)
            i += 1
            j += 1

        for i in range(0, n):
            if grumpy[i] == 0:
                maxUnSatisfy += customers[i]

        return maxUnSatisfy
