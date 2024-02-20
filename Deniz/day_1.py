class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        opening = ['(', '[' ,'{']
        closing = [')', ']' ,'}']
        for i in s:
            if i in opening:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False 
                elif closing.index(i) == opening.index(stack[-1]):
                    stack.pop()
                else:
                    return False 

        return len(stack) == 0
