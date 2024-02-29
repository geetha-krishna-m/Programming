# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [(root, 0)]
        current_value = 0
        current_index = 0
        # breadth-first search algorithm
        while queue:
            root, index = queue.pop(0)
            # even index
            if index % 2 == 0:
                # value should be odd
                if root.val % 2 == 0:
                    return False
                # any node in the same even index should be bigger than last
                if index == current_index and root.val <= current_value:
                    return False
            # odd index
            else:
                # value should be even
                if root.val % 2 != 0:
                    return False
                # any node in the same odd index should be less than last
                if index == current_index and root.val >= current_value:
                    return False
            # update the value and index
            current_index = index
            current_value = root.val
            if root.left:
                queue.append((root.left, index + 1))
            if root.right:
                queue.append((root.right, index + 1))
        return True