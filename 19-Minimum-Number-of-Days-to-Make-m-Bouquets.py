# question https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/?envType=daily-question&envId=2024-06-19

# Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
# Output: 3
# Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
# We need 3 bouquets each should contain 1 flower.
# After day 1: [x, _, _, _, _]   // we can only make one bouquet.
# After day 2: [x, _, _, _, x]   // we can only make two bouquets.
# After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.


class Solution(object):
    def minDays(self, bloomDay, m, k):
        if len(bloomDay) < m * k:
            return -1

        def minmax(arr):
            minVal = float("infinity")
            maxVal = 0

            for elem in arr:
                minVal = min(minVal, elem)
                maxVal = max(maxVal, elem)
            return {"minVal": minVal, "maxVal": maxVal}

        def ispossible(arr, mid, m, k):
            noOfBloom = 0
            count = 0

            for elem in arr:
                if elem <= mid:
                    count += 1
                else:
                    noOfBloom += count // k
                    count = 0
            noOfBloom += count // k
            return noOfBloom >= m

        obj = minmax(bloomDay)
        low = obj["minVal"]
        high = obj["maxVal"]
        answer = -1

        while low <= high:
            mid = (low + high) // 2
            if ispossible(bloomDay, mid, m, k):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer
