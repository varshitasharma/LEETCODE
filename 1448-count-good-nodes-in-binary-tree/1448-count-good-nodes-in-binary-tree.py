# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, maxm):
            if not root:
                return 0
            ans = 1 if root.val >= maxm else 0
            return ans + helper(root.left, max(maxm, root.val)) + helper(root.right, max(maxm, root.val))
        return helper(root,-10001)
        
#         count = 0
#         def helper(root, maxm):
#             nonlocal count
#             if not root:
#                 return
#             if root.val >=maxm:
#                 count += 1
            
#             helper(root.left, max(maxm, root.val))
            
#             helper(root.right, max(maxm, root.val))
#         helper(root,-10001)
#         return count
                    
                    