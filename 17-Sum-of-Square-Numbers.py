# quetion link :- https://leetcode.com/problems/sum-of-square-numbers/description/?envType=daily-question&envId=2024-06-17

# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5

# Time Complexity :O(√c) , Space Complexity  O(√c)  not optimal

def judgeSquareSum(self, c):
    sqrArray = set()

    for elem in range(int(sqrt(c)) + 1):
        sqrArray.add(elem * elem)
    print(sqrArray)

    a = 0
    while a * a <= c:
        b = c - a * a
        if b in sqrArray:
            return True
        a += 1
    return False

# two pointer approach 
class Solution(object):
    def evaluate(self, a, b):
        return a*a + b*b

    def judgeSquareSum(self, c):
        l = 0
        r = int(sqrt(c))
        while l <= r:
            val = self.evaluate(l, r)
            if val == c:
                return True
            elif val > c:
                r -= 1
            else:
                l += 1
        return False
