# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        val = 0
        for operation in operations:
            match operation:
                case "--X":
                    val -= 1
                case "X--":
                    val -= 1
                case "X++":
                    val += 1
                case "++X":
                    val += 1
        return val


s = Solution()
operations = ["X++", "++X", "--X", "X--"]
print(s.finalValueAfterOperations(operations))
