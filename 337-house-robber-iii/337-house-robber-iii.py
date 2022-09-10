# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.dfs(root))
    def dfs(self, root):
        if not root: return (0,0)
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return (root.val + left[1] + right[1], max(left[0],left[1]) + max(right[0],right[1]))
         
    """
    Input: [3,4,5,1,3,null,1]
 input tree            dp tree:
     3                  [3+3+1,4+5]
    / \                /        \
   4   5            [4,3]      [5,1]
  / \   \          /     \          \
 1   2   1      [1,0]    [2,0]     [1,0]
                / \       /  \        /  \
           [0,0] [0,0] [0,0] [0,0]  [0,0] [0,0]
    
    """
        
    '''we construct a dp tree, each node in dp tree represents [rob the current node how much you gain, skip the     current node how much you gain]
    dp_node[0] =[rob the current node how much you gain]
    dp_node[1] =[skip the current node how much you gain]
    we start the stolen from the leaf: Depth First Search
    for each node you have 2 opitions:
    option 1: rob the node, then you can't rob the child of the node.
    dp_node[0] = node.val + dp_node.left[1] +dp_node.right[1]
    option 2: skip the node, then you can rob or skip the child of the node.
    dp_node[1] = dp_node.left[0] + dp_node.right[0]
    the maximum of gain of the node depents on max(dp_node[0],dp_node[1])'''