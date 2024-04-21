# https://leetcode.com/problems/find-the-maximum-achievable-number/

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + t * 2


num = 3
t = 2
s = Solution()
print(s.theMaximumAchievableX(num, t))
