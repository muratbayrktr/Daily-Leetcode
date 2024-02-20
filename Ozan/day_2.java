// Solution for 74. Search a 2D Matrix
// link: https://leetcode.com/problems/search-a-2d-matrix/description/

class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int numberOfRows = matrix.length;
        int numberOfColumns = matrix[0].length;
        
        // 1. find row
        int first = 0;
        int last = numberOfRows -1;
        int rowIndex = (last + first)/2;

        while (first<=last) {
            if (matrix[rowIndex][0]<=target && target<=matrix[rowIndex][numberOfColumns-1])
                break;

            if (matrix[rowIndex][0]>target) {
                last = rowIndex - 1;
                rowIndex = (first+last)/2;
            } else if (matrix[rowIndex][0]<target) {
                first = rowIndex + 1;
                rowIndex = (first+last)/2;
            } 
        }

        // 2. find column
        first = 0;
        last = matrix[0].length-1;
        int indexOfMiddle = (last + first)/2;
        
        boolean res = false;
        while (first<=last) {
            if (matrix[rowIndex][indexOfMiddle]==target) {
                res = true;
                break;
            }

            if (matrix[rowIndex][indexOfMiddle]>target) {
                last = indexOfMiddle - 1;
                indexOfMiddle = (first+last)/2;
            } else if (matrix[rowIndex][indexOfMiddle]<target) {
                first = indexOfMiddle + 1;
                indexOfMiddle = (first+last)/2;
            }
        }
        
        return res;
    }
}