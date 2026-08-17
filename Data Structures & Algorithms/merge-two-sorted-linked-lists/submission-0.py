# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ## simple edge case
        if list1 is None:
            if list is None:
                return None
            else:
                return list2
        elif list2 is None:
            return list1
            
        list3 = ListNode()
        curr = list3

        curr1 = list1
        curr2 = list2

        while(curr1 and curr2):
            if curr1.val < curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next
        if curr1 is None:
            curr.next = curr2
        else:
            curr.next = curr1
        print(list3)
        list3 = list3.next
        return list3
