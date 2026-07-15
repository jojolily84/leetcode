"""
這題本質是 graph traversal：把每個 room 當作一個 node，room 裡的 key 當作指向其他 node 的 edge。
從 room 0 開始做 DFS(stack)/BFS(deque)，能走到的 node 就是能進入的 room。
最後檢查 visited 數量是否等於 n。
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = {0}  #記錄已進入的 room
        stack = [0]  #尚未 visited 的 key
        
        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)  #在 push 進 stack 的當下就標記，避免重複進入 stack
                    stack.append(key)
        return len(visited) == n

"""
from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = {0}  #記錄已進入的 room
        queue = deque([0])
        while queue:
            room = queue.popleft()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)
        return len(visited) == n
"""
