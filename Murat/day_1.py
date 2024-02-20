s = "{[]}"

class Solution:
    # https://leetcode.com/problems/valid-parentheses/submissions/1180235993
    def isValid(self, s: str) -> bool:
        dimensions = [0,0,0,[]]
        for i in s:
            if i == "(":
                dimensions[0] += 1
                dimensions[3].append(0)
            elif i == ")":
                if dimensions[3][-1] == [] or dimensions[3][-1] != 0:
                    return False
                dimensions[3].pop()
                dimensions[0] -= 1
            elif i == "[":
                dimensions[1] += 1
                dimensions[3].append(1)
            elif i == "]":
                if dimensions[3][-1] == [] or dimensions[3][-1] != 1:
                    return False
                dimensions[3].pop()
                dimensions[1] -= 1
            elif i == "{":
                dimensions[2] += 1
                dimensions[3].append(2)
            elif i == "}":
                if dimensions[3][-1] == [] or dimensions[3][-1] != 2:
                    return False
                dimensions[3].pop()
                dimensions[2] -= 1
            if dimensions[0] < 0 or dimensions[1] < 0 or dimensions[2] < 0:
                return False
        if dimensions[0] == 0 and dimensions[1] == 0 and dimensions[2] == 0:
            return True
        
sol = Solution()
print(sol.isValid(s))