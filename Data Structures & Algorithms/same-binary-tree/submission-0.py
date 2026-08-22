# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ## recursion done, theyre same!
        if p is None and q is None:
            return True
        ## only 1 is done, diff
        if p is None or q is None:
            return False
        ## if compared vals diff, diff
        if q.val != p.val:
            return False
        ## use recursion to check both left and right
        if q.val == p.val:
            return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        