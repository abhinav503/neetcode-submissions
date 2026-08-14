# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head and head.next:
            slow = head 
            fast = head.next
            while (fast and slow) and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
            curr = None
            if slow:
                curr = slow.next
                slow.next = None
            prev = None
            while curr:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            
            while head and prev:
                rightNext = prev.next
                leftNext = head.next
                head.next = prev
                prev.next = leftNext
                prev = rightNext
                head = leftNext

            


