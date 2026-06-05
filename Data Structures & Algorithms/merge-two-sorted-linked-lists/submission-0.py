# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = list1
        c2 = list2
        newListStart = ListNode(val=-1)
        newList = newListStart
        while c1 is not None and c2 is not None:
            if c1.val > c2.val:
                newList.next = c2
                newList = newList.next
                c2 = c2.next
            elif c1.val <= c2.val:
                newList.next = c1
                newList = newList.next
                c1 = c1.next
            
        while c1 is not None:
            newList.next = c1
            newList = newList.next
            c1 = c1.next
        while c2 is not None:
            newList.next = c2
            newList = newList.next
            c2 = c2.next

        return newListStart.next