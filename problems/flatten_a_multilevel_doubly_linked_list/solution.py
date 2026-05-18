"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(node):
            curr = node
            last = node
            while curr:
                next_node = curr.next
                if curr.child:
                    child_head = curr.child
                    child_tail = dfs(child_head)
                    curr.next = child_head
                    child_head.prev = curr
                    
                    if next_node:
                        child_tail.next = next_node
                        next_node.prev = child_tail
                    curr.child = None
                    last = child_tail
                else:
                    last = curr
                curr = next_node
            return last
        if not head:
            return head
        
        dfs(head)
        return head