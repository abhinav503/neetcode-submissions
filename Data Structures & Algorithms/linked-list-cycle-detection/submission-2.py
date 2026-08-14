# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowHead , fastHead= head, head
        while (fastHead and slowHead) and fastHead.next:
            slowHead = slowHead.next
            fastHead = fastHead.next.next
            if slowHead == fastHead:
                return True
        return False
