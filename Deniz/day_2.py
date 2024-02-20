class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        return self.binarySearch(matrix, target, 0, m * n - 1, n)
    
    def binarySearch(self, matrix, target, left, right, n):
        if left > right:
            return False
        
        mid = (left + right) // 2
        mid_value = matrix[mid // n][mid % n]
        
        if target == mid_value:
            return True
        elif target < mid_value:
            return self.binarySearch(matrix, target, left, mid - 1, n)
        else:
            return self.binarySearch(matrix, target, mid + 1, right, n)