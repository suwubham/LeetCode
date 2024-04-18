class Solution:
    def balancedStringSplit(self, s: str) -> int:
        b = 0
        count = 0
        for letter in s:
            if letter == "L":
                b += 1
            else:
                b -= 1
            if b == 0:
                count += 1
        return count


s = Solution()
word = "RLRRLLRLRL"
print(s.balancedStringSplit(word))
