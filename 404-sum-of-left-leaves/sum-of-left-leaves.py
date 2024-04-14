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
        def sums(root,prev,sumy):
            if root == None:
                return sumy
            if root.left == None and root.right == None and prev.left == root:
                sumy += root.val
                return sumy
            return sums(root.left,root,sumy) + sums(root.right,root,sumy)
        return sums(root,root,0)