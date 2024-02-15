# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sums,flag = 0,False
        def has(root):
            nonlocal sums,flag
            if root == None:
                return
            sums += root.val
            has(root.left)
            has(root.right)
            if(root.left == None and root.right == None and sums == targetSum):
                flag = True
            sums -= root.val
        has(root)
        return flag