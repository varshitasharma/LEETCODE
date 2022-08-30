# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = head.next, head
        left = ptr2
        while( ptr1 != None):
            if ptr1.val == 0:
                left, cur_sum, ptr2 = ptr2, 0, ptr2.next
                while(ptr2 != ptr1):
                    cur_sum += ptr2.val
                    ptr2 = ptr2.next
                left.val = cur_sum
                left.next = ptr2
                # print(left)
            ptr1 = ptr1.next
        left.next = None
        return head
            
                    
                
                    
            