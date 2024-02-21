// Solution for 78. Subsets
// link: https://leetcode.com/problems/subsets/description/

class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> accumulate = new ArrayList<>();

        helper(result,nums,0,accumulate);
        return result;
    }

    public void helper(List<List<Integer>> result, int[] nums, int index, List<Integer> accumulate) {
        if (index==nums.length) {
            result.add(accumulate);
            return;
        }
        
        List<Integer> withAddition = new ArrayList<>(accumulate);
        withAddition.add(nums[index]);
        List<Integer> withoutAddition = new ArrayList<>(accumulate);
        
        helper(result,nums,index+1,withAddition);
        helper(result,nums,index+1,withoutAddition);
    }
}