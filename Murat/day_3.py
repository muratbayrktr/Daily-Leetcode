nums = [1,2,3]


class Solution:
    # https://leetcode.com/problems/subsets/submissions/1182428134
    def subsets(self, nums: list[int]) -> list[list[int]]:
        if not nums: return []
        base = nums[0]
        subrest = self.subsets(nums[1:])
        if subrest: return ([*[[base]+x for x in subrest], *subrest])
        else: return ([subrest] + [[base] + subrest])



sol = Solution()
print(sol.subsets(nums))
