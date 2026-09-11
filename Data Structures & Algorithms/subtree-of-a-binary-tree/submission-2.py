# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root, subRoot):
            if root is None and subRoot is None:
                return True

            if root is None or subRoot is None:
                return False

            if subRoot.val != root.val:
                return False
            
            return sameTree(root.right, subRoot.right) and sameTree(root.left, subRoot.left)
        
        ## base cases
        if root is None and subRoot is None:
            return True
        
        if root is None or subRoot is None:
            return False
        
        ## check if roots have same val
        ## check if sameTree returns true
        if root.val == subRoot.val and sameTree(root, subRoot):
            return True
        ## else recurse through og tree
        else:
            return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)