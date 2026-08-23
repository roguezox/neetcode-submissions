class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        cto = {")":"(","]":"[","}":"{"}
        for i in s:
            if i in cto:
                if stack and stack[-1] == cto[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False