# https://leetcode.com/problems/build-array-from-permutation/

from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        val = [0] * (len(nums))
        for i in range(len(val)):
            val[i] = nums[nums[i]]
        return val

    def buildArray2(self, nums: List[int]) -> List[int]:
        # one liner
        return [nums[i] for i in nums]

    # Todo: Solution in constant space


s = Solution()
nums = [0, 2, 1, 5, 3, 4]
print(s.buildArray2(nums))
