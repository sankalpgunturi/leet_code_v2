class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s) < 2:
        #     return False
        closeToOpen = {'}':'{', ')':'(', ']':'['}
        stack = []
        for c in s:
            if c in closeToOpen.values():
                stack.append(c)
            else:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        