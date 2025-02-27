# https://leetcode.com/problems/contains-duplicate/

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for v in count.values():
            if v > 1:
                return True
        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)


s = Solution()

print(s.containsDuplicate([1, 2, 3, 1]))
