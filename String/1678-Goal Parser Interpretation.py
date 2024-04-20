# https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command: str) -> str:
        code = {
            "G": "G",
            "()": "o",
            "(al)": "al"
        }
        op = ""
        temp = ""
        for letter in command:
            if letter not in code:
                temp += letter
            if letter in code:
                op += code[letter]
            if temp in code:
                op += code[temp]
                temp = ""
        return op

    def interpret2(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")


command = "(al)G(al)()()G"
s = Solution()
print(s.interpret2(command))
