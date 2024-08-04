/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean traverse(TreeNode root,int pathSum,int targetSum){
    if(root == null){
        return false;
    }
    pathSum = pathSum + root.val;
    if((root.left == null) && (root.right == null))
        return pathSum == targetSum;
    return traverse(root.left,pathSum,targetSum) || traverse(root.right,pathSum,targetSum);
    }
    public boolean hasPathSum(TreeNode root, int targetSum) 
    {
        if(root != null)
          return traverse(root,0,targetSum);
        return false;
    }
}