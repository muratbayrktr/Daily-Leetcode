class Solution:
    # https://leetcode.com/problems/product-of-array-except-self/submissions/1184195792
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1]*length
        leftprod = 1
        rightprod = 1
        for i in range(length):
            answer[i] = answer[i]*leftprod
            leftprod *= nums[i]
        for i in range(length-1, -1, -1):
            answer[i] = answer[i]*rightprod
            rightprod *= nums[i]
        return answer