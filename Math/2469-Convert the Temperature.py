# https://leetcode.com/problems/convert-the-temperature/description/

from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.8 + 32.00]


celsius = 36.50
s = Solution()
print(s.convertTemperature(celsius))
