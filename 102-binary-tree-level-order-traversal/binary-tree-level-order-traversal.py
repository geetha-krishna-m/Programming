# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        final = []
        if root is None:
            return final
        q = [[root]]
        while q:
            eles = q.pop(0)
            if eles:
                final.append([])
                q.append([])
                for ele in eles:
                    final[-1].append(ele.val)
                    if ele.left is None and ele.right is None:
                        continue
                    if ele.left!=None:
                        q[-1].append(ele.left)
                    if ele.right!=None:
                        q[-1].append(ele.right)
        return final