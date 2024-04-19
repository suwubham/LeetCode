# https://leetcode.com/problems/find-words-containing-character/

from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        sol = []
        for index, word in enumerate(words):
            if x in word:
                sol.append(index)
        return sol


words = ["abc", "bcd", "aaaa", "cbc"]
x = "a"
s = Solution()
print(s.findWordsContaining(words, x))
