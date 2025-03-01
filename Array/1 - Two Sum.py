# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement not in hash:
                hash[num] = index
            else:
                return [hash[complement], index]
        return "Not found"

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i1, num1 in enumerate(nums):
            complement = target - num1
            for i2, num2 in enumerate(nums):
                if i1 != i2:
                    if num2 == complement:
                        return [i1, i2]
        return "Not found"


s = Solution()
print(s.twoSum2([2, 7, 11, 15], 9))  # [0,1]
