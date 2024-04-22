# https://leetcode.com/problems/maximum-odd-binary-number/description/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = list(s)
        for index, num in enumerate(s):
            if num == "1":
                s[index], s[-1] = s[-1], s[index]
                print("A")
                break

        max = 0
        for i in range(len(s) - 1):
            if s[i] == "1":
                s[i], s[max] = s[max], s[i]
                max += 1
        return "".join(s)


a = "0101"
s = Solution()
print(s.maximumOddBinaryNumber(a))
