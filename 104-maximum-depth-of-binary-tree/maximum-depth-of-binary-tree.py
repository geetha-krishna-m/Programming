# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         maxy = 0
#         def traverse(root,curr_max):
#             nonlocal maxy
#             if root == None:
#                 maxy = curr_max if curr_max > maxy else maxy
#                 curr_max -= 1
#                 return maxy
#             left = traverse(root.left,curr_max + 1)
#             right = traverse(root.right,curr_max + 1)
#             return right
#         return traverse(root,0)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxy = 0
        def traverse(root,curr_max):
            nonlocal maxy
            if root == None:
                return
            traverse(root.left,curr_max+1)
            traverse(root.right,curr_max+1)
            maxy = max(maxy,curr_max)
        traverse(root,1)
        return maxy