# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        return count


s = Solution()
jewels = "aA"
stones = "aAAbbbb"
print(s.numJewelsInStones(jewels, stones))
