class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            currentSize = len(result)
            for i in range(currentSize):
                newSubset = result[i][:] + [num]
                result.append(newSubset)

        return result