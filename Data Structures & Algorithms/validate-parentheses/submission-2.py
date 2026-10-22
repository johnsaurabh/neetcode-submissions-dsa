class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        bracket_map={"}":"{","]":"[",")":"("}

        for char in s:
            if char in {"{","[","("}:
                stack.append(char)
            elif not stack or bracket_map[char]!=stack.pop():
                return False
        return len(stack)==0

