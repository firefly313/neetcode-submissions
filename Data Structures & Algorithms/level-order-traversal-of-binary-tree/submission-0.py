# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:        

        ## base case
        if root is None:
            return []
        
        queue = [root]
        lvl_order = []

        while queue:
            level = []
            level_size = len(queue)
            for _ in range(level_size):
                curr = queue.pop(0)
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            lvl_order.append(level)  

        return lvl_order
