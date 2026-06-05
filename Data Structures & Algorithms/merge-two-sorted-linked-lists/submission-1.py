# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1, c2 = list1, list2
        newListStart = ListNode(val=-1)
        newList = newListStart
        while c1 is not None and c2 is not None:
            if c1.val > c2.val:
                newList.next = c2
                c2 = c2.next
            else:
                newList.next = c1
                c1 = c1.next
            newList = newList.next
            
        newList.next = c1 if c1 is not None else c2
        return newListStart.next