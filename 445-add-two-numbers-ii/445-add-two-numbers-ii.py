# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''Without reversing the list'''
        n1, n2 = 0, 0
        curr1, curr2, prev = l1, l2,None
        while(curr1):
            curr1 =curr1.next
            n1 +=1
        while(curr2):
            curr2 =curr2.next
            n2 +=1
        curr1, curr2 = l1, l2
        
        # parse both lists
        # and sum the corresponding positions 
        # without taking carry into account
        # 3->3->3 + 7->7 --> 3->10->10 --> 10->10->3
        while(n1>0 and n2>0):
            val = 0
            if n1 >= n2:
                val += curr1.val
                curr1 = curr1.next
                n1-=1
            if n1 < n2:
                val += curr2.val
                curr2 = curr2.next
                n2-=1
             
            # update the result: add to front
            curr = ListNode(val)
            curr.next = prev
            prev = curr
            
         # take the carry into account
        # to have all elements to be less than 10
        # 10->10->3 --> 0->1->4 --> 4->1->0
        carry,  prev = 0, None
        while(curr):
            carry, val = divmod(curr.val+carry, 10)
            # update the result: add to front
            newNode = ListNode(val, prev)
            prev = newNode
            # move to the next elements in the list
            curr = curr.next
        # add the last carry
        if carry:
            newNode = ListNode(carry, prev)
        return newNode
        
        
        
        
        '''Reverse both the lists and store ans by traversing the lists'''
#         if l1.next:
#             curr, nextNode = l1, l1.next
#             nextNode.next, curr.next, curr,nextNode  = curr, None, nextNode, nextNode.next
#             while(nextNode):
#                 nextNode.next, curr, nextNode = curr, nextNode, nextNode.next
#             l1 = curr
#         if l2.next:
#             curr, nextNode = l2, l2.next
#             nextNode.next, curr.next, curr,nextNode  = curr, None, nextNode, nextNode.next
#             while(nextNode):
#                 nextNode.next, curr, nextNode = curr, nextNode, nextNode.next
#             l2 = curr
  
#         carry = 0
#         prev = None
#         while(l1!=None or l2!=None or carry!=0):
#             val1 = l1.val if l1 else 0
#             val2 = l2.val if l2 else 0
#             curSum = val1 + val2 + carry
#             carry, nodeVal = divmod(curSum, 10)
#             curr = ListNode(nodeVal)
#             curr.next = prev
#             prev = curr
#             # print(l1.val)
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
#         return curr
    