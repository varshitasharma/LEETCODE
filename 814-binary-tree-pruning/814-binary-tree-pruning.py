# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
        if self.helper(root) == False: return None
        
        return root
    def helper(self,root):
        if root:
            left = self.helper(root.left)
            right = self.helper(root.right)
            if left == False : root.left = None
            if right == False: root.right = None
            # print(root.val or left or right)
            return root.val or left or right
        return False