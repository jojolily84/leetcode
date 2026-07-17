"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next  #linked list
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        curr = root
        while curr:          # 外層：每跑一次 = 處理一層
            dummy = Node(0)  # 每次進入外層迴圈，都建立一個全新的、跟 root 無關的節點
            tail = dummy     # 下一層目前串到的最後一個節點
            
            while curr:      # 內層：在「當前層」內往右移動
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next  # 移到當前層的下一個節點
            curr = dummy.next     # 內層跑完，cur 換成「下一層的第一個節點」
        return root
