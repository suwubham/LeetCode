# https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "[.]".join(address.split("."))


s = Solution()
address = "1.1.1.1"
print(s.defangIPaddr(address))
