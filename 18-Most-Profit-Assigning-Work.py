# question https://leetcode.com/problems/most-profit-assigning-work/description/?envType=daily-question&envId=2024-06-18
def maxProfitAssignment(self, difficulty, profit, worker):
    jobs = sorted(zip(difficulty, profit))
    res = i = best = 0
    for ability in sorted(worker):
        while i < len(jobs) and ability >= jobs[i][0]:
            best = max(jobs[i][1], best)
            i += 1
        res += best
    return res