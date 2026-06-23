class ListNode:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        
class MyHashMap:

    def __init__(self):
        self.SIZE = 1009  # 選質數，減少碰撞
        self.buckets = [None] * self.SIZE
    
    def _hash(self,key):
        return key % self.SIZE

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        node = self.buckets[idx]
        
        # 用 dummy head 簡化 edge case
        dummy = ListNode(-1, -1)
        dummy.next = node
        curr = dummy
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = ListNode(key, value)
        self.buckets[idx] = dummy.next
        
    def get(self, key: int) -> int:
        idx = self._hash(key)
        curr = self.buckets[idx]
        
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        dummy = ListNode(-1, -1)
        dummy.next = self.buckets[idx]
        curr = dummy
        
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next  # 跳過目標 node
                break
            curr = curr.next
            
        self.buckets[idx] = dummy.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
