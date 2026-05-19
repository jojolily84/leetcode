# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 空 linked list 或不用轉
        if not head or not head.next or k == 0:
            return head
        # 1. 算 linked list 長度
        length = 1
        tail = head
        while tail.next:
            tail =tail.next
            length += 1
        # 2. 避免多餘旋轉
        k = k % length
        # 如果剛好轉回原樣
        if k == 0:
            return head
        # 3. 尾巴接回頭，形成環
        tail.next = head
        # 4. 找新的尾巴 新尾巴在第 length-k-1 個位置
        steps = length - k
        new_tail = head
        for _ in range(steps-1):
            new_tail = new_tail.next
            
        new_head = new_tail.next
        new_tail.next = None
        return new_head