# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        def ins(root):
            if(root == None):
                return 
            ins(root.left)
            l.append(root.val)
            ins(root.right)
        ins(root)
        return l
        
    
        