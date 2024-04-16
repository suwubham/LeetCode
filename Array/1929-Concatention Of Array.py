# https://leetcode.com/problems/concatenation-of-array/

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums+nums

    def getConcatenation2(self, nums: List[int]) -> List[int]:
        arr = [0] * (2 * len(nums))
        for i in range(len(nums)):
            arr[i] = nums[i]
            arr[i+len(nums)] = nums[i]
        return arr


s = Solution()
print(s.getConcatenation2([1, 2, 3, 4, 5]))
