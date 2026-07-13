"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_to_new = {}
        
        def dfs(n):
            if n in old_to_new:
                return old_to_new[n]
            
            clone = Node(n.val)
            old_to_new[n] = clone  #在遞迴進入下一層之前，先把當前狀態記錄下來
            
            for neighbor in n.neighbors:
                clone.neighbors.append(dfs(neighbor))
                
            return clone
        return dfs(node)
