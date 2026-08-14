# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        print(head)
        #if head.len == 0:
        #    return head
        #head = head[-1]
        curr, prev = head, None
        
        while curr:
            temp = curr.next
            ## curr next now points to the previous point
            curr.next = prev
            ## iteration part so itll point correctly next lop
            prev = curr
            ## iteration to go to the next number
            curr = temp
        return prev


        ## curr = next
        ## head = -1

