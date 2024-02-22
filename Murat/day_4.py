class Solution:
    # https://leetcode.com/problems/same-tree/submissions/1183274479
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and not q): return True
        if (not p or not q): return False
        
        if p.val != q.val: return False
        r, l = True, True
        r = self.isSameTree(p.left,q.left)
        l = self.isSameTree(p.right,q.right)
        
        return r and l