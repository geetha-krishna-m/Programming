# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root,i):
            if(not root):
                return
            if(i<=len(res)-1):
                res[i] = root.val
            else:
                res.append(root.val)
            dfs(root.left,i+1)
            dfs(root.right,i+1)
        dfs(root,0)
        return res

