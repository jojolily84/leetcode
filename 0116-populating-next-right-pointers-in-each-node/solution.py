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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        leftmost = root
        # <垂直>當 leftmost 還有 left child，代表下面還有一層要處理
        while leftmost.left:
            curr = leftmost
            while curr:
                # 連接：同一個 parent 底下的 left -> right
                curr.left.next = curr.right
                # <水平>在同一層裡，curr 右邊還有沒有下一個 parent 的 left
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            leftmost = leftmost.left
        return root
