# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root == None:
            return True

        def dfs(root):
            if root is None:
                return 0
            right_height = dfs(root.right)
            left_height = dfs(root.left)

            if left_height == -1 or right_height == -1:
                return -1

            if abs(right_height - left_height) > 1:
                return -1
            
            return 1 + max(left_height, right_height)
        
        if dfs(root) == -1:
            return False

        return True