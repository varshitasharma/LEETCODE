# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # print(l1,l2)
        
        if l1.next:
            curr, nextNode = l1, l1.next
            nextNode.next, curr.next, curr,nextNode  = curr, None, nextNode, nextNode.next
            while(nextNode):
                nextNode.next, curr, nextNode = curr, nextNode, nextNode.next
            l1 = curr
        
        if l2.next:
            curr, nextNode = l2, l2.next
            nextNode.next, curr.next, curr,nextNode  = curr, None, nextNode, nextNode.next
            while(nextNode):
                nextNode.next, curr, nextNode = curr, nextNode, nextNode.next
            l2 = curr
        # print(l1,l2)
        carry = 0
        prev = None
        
        # print(l1,l2)
        while(l1!=None or l2!=None or carry!=0):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            curSum = val1 + val2 + carry
            carry, nodeVal = divmod(curSum, 10)
            curr = ListNode(nodeVal)
            curr.next = prev
            prev = curr
            # print(l1.val)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return curr
#         if dummy and dummy.next:
#             curr, nextNode = dummy, dummy.next
#             nextNode.next, curr.next, curr,nextNode  = curr, None, nextNode, nextNode.next
#             while(nextNode):
#                 nextNode.next, curr, nextNode = curr, nextNode, nextNode.next
#             return curr
#         return dummy
        