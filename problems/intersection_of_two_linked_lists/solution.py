# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        startA = headA
        startB = headB
        while headA != headB:
            headA = headA.next if headA else startB
            headB = headB.next if headB else startA
        return headA