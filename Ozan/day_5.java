// Solution for 238. Product of Array Except Self
// link: https://leetcode.com/problems/product-of-array-except-self/description/


class Solution {
    public int[] productExceptSelf(int[] nums) {
        int sizeOfArray = nums.length;
        int[] prefix = new int[sizeOfArray];
        int[] postfix = new int[sizeOfArray];

        int acc = 1;
        for (int i=0; i<sizeOfArray; i++) {
            acc *= nums[i];
            prefix[i] = acc;
        }

        acc = 1;
        for (int i=sizeOfArray-1; i>=0; i--) {
            acc *= nums[i];
            postfix[i] = acc;
        }

        int[] result = new int[sizeOfArray];
        for (int i=1; i<sizeOfArray-1; i++) {
            result[i] = prefix[i-1] * postfix[i+1];
        }

        result[0] = postfix[1];
        result[sizeOfArray-1] = prefix[sizeOfArray-2];

        return result;
    }
}