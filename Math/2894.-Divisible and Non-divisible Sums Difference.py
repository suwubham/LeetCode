# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return sum([i for i in range(1, n+1) if i % m != 0]) - sum([i for i in range(1, n+1) if i % m == 0])


s = Solution()
print(s.differenceOfSums(n=5, m=6))
