# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            curr, nextNode = head, head.next
            nextNode.next, curr.next, curr,nextNode  = curr, None, nextNode, nextNode.next
            while(nextNode):
                nextNode.next, curr, nextNode = curr, nextNode, nextNode.next
            return curr
        return head