matrix = [[1]] #[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 1


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row_mid = len(matrix) // 2
        if len(matrix) == 0:
            return False
        if len(matrix) == 1:
            return self.row_binary_search(matrix[0], target)
        else:
            if matrix[row_mid][0] == target:
                return True
            elif matrix[row_mid][0] > target:
                # Upper half recursive call
                return self.searchMatrix(matrix[:row_mid], target)
            elif matrix[row_mid][0] < target:
                # Lower half or same row
                if matrix[row_mid][-1] < target:
                    # Lower half recursive call
                    return self.searchMatrix(matrix[row_mid:], target)
                elif matrix[row_mid][-1] >= target:
                    # Current row binary search 
                    return self.row_binary_search(matrix[row_mid], target)

    def row_binary_search(self, array, target):
        mid = len(array)//2
        if len(array) == 0:
            return False
        if array[mid] > target:
            # left
            return self.row_binary_search(array[:mid], target)

        elif array[mid] == target:
            return True
        
        elif array[mid] < target:
            # right
            return self.row_binary_search(array[mid+1:], target)


sol = Solution()
print(sol.searchMatrix(matrix, target))
