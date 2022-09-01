# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def helper(root, maxm):
            nonlocal count
            if not root:
                return
            if root.val >=maxm:
                count += 1
            
            helper(root.left, max(maxm, root.val))
            
            helper(root.right, max(maxm, root.val))
        helper(root,-10001)
        return count
                    
                    