# https://leetcode.com/problems/number-of-good-pairs/solutions/

from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if (nums[i] == nums[j]) & ((j, i) not in count):
                        count.append((i, j))
        return len(count)


s = Solution()
nums = [1, 2, 3, 1, 1, 3]
print(s.numIdenticalPairs(nums))
