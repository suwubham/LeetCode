# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

class Solution:
    def minimumSum(self, num: int) -> int:
        w = [int(x) for x in str(num)]
        l1 = w.pop(w.index(min(w)))
        l2 = w.pop(w.index(min(w)))
        l3 = w.pop(w.index(min(w)))
        l4 = w.pop(w.index(min(w)))
        return int(f"{l1}{l3}") + int(f"{l2}{l4}")


s = Solution()
num = 2932
print(s.minimumSum(num))
