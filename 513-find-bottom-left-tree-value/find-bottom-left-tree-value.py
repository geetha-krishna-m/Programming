# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        d = dict()
        cnt = 0
        def traverse(root):
            nonlocal cnt
            if root == None:
                return
            cnt = cnt + 1
            traverse(root.left)
            if cnt not in d:
                d[cnt] = root.val
            traverse(root.right)
            cnt -= 1
        traverse(root)
        return d[max(d)]