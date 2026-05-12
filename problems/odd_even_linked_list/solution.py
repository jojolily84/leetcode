# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: #空鍊表或只有一個節點
            return head
        odd = head
        even = head.next
        even_head = even    # 保存偶數開頭
        while even and even.next: #只要檢查even跟even.next odd跟odd.next就會存在
            odd.next = even.next
            odd = odd.next
        
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head