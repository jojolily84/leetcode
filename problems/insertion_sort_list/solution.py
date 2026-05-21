# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy: 排序後串列的起點
        dummy = ListNode(0)
        curr = head
        while curr:
            next_node = curr.next
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            # 插入 curr
            curr.next = prev.next  #先接後面
            prev.next = curr  #再接前面
            curr = next_node #下一個
        return dummy.next