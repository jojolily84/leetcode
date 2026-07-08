import random
class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.idx_map = {}  #記錄 val -> arr 中的 index

    def insert(self, val: int) -> bool:
        if val in self.idx_map:
            return False
        self.idx_map[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx_map:
            return False
        idx = self.idx_map[val]
        last_val = self.arr[-1]
        # 把最後一個元素複製到要刪除的位置
        self.arr[idx] = last_val
        self.idx_map[last_val] = idx
        # 刪除尾端元素與舊的 map entry
        self.arr.pop()
        del self.idx_map[val]  #刪除 val:idx 這組值
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
