# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if(not root):
            return []
        queue = [root]
        res = []
        while queue:
            n = len(queue)
            res.append(queue[-1].val)
            for i in range(n):
                root = queue.pop(0)
                if(root.left):
                    queue.append(root.left)
                if(root.right):
                    queue.append(root.right) 
        return res
            
            
