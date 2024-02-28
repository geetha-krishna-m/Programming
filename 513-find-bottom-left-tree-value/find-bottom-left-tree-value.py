# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        finalRes = root.val
        cnt,cCnt = 0,0
        def traverse(root):
            nonlocal cnt,cCnt,finalRes
            if root == None:
                return
            cnt = cnt + 1
            traverse(root.left)
            if cnt > cCnt:
                finalRes = root.val
                cCnt = cnt
            traverse(root.right)
            cnt -= 1
        traverse(root)
        return finalRes