class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_arr = [1] * n
        post_arr = [1] * n
        res = [1] * n

        prefix = 1
        for i in range(n):
            pre_arr[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n-1, -1, -1):
            post_arr[i] = postfix
            postfix *= nums[i]

        for i in range(n):
            res[i] = pre_arr[i] * post_arr[i]

        return res