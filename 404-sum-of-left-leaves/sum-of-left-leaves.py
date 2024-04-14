# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        sumy = 0
        def sums(root,prev):
            nonlocal sumy
            if root == None:
                return 
            if root.left == None and root.right == None and prev.left == root:
                sumy += root.val
            sums(root.left,root)
            sums(root.right,root)
        sums(root,root)
        return sumy
