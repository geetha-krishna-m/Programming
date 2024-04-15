class Solution:
    # Function to calculate the sum of numbers formed by root to leaf paths
    def sumNumbers(self, root: TreeNode, currentSum: int = 0) -> int:
        # Base case: if the node is None, return 0
        if root is None:
            return 0
        # Update the current sum by appending the current node's value
        currentSum = currentSum * 10 + root.val
        # If the node is a leaf node, return the sum formed by the path
        if root.left is None and root.right is None:
            return currentSum
        # Recursively calculate the sum for left and right subtrees
        return self.sumNumbers(root.left, currentSum) + self.sumNumbers(root.right, currentSum)