"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        output = []
        if root:
            q = deque([root])
            while(q):
                level = []
                for i in range(len(q)):
                    cur = q.popleft()
                    level.append(cur.val)
                    children = cur.children
                    for child in children:
                        if children:
                            q.append(child)
                output.append(level)
        return output
                    
                
        