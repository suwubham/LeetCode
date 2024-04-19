# https://leetcode.com/problems/shuffle-the-array/
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        p1 = nums[:n]
        p2 = nums[n:]
        final = []
        for i in range(n*2):
            final.append(p1.pop(0)) if i % 2 == 0 else final.append(p2.pop(0))
        return final

    def shuffle2(self, nums: List[int], n: int) -> List[int]:
        pl = 0
        pr = 0
        final = []
        for i in range(n*2):
            if i % 2 == 0:
                final.append(nums[pl])
                pl += 1
            else:
                final.append(nums[pr+n])
                pr += 1

        return final


s = Solution()
nums = nums = [2, 5, 1, 3, 4, 7]
n = 3
print(s.shuffle2(nums, n))
