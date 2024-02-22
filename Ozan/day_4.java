// Solution for 100. Same Tree
// link: https://leetcode.com/problems/same-tree/description/


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p==null && q==null)
            return true;
        boolean comparison = (p!=null && q==null) || (p==null && q!=null) || (p.val!=q.val);
        if (comparison)
            return false;

        return isSameTree(p.left,q.left) && isSameTree(p.right,q.right);
    }
}