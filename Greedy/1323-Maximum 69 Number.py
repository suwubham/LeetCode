# https://leetcode.com/problems/maximum-69-number/

class Solution:
    def maximum69Number(self, num: int) -> int:
        numm = list(str(num))
        for index, n in enumerate(numm):
            if n == "6":
                numm[index] = "9"
                break
        return int("".join(numm))


num = 9669
s = Solution()
print(s.maximum69Number(num))
