class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for l, r, h in buildings:
            events.append((l,-h)) #進場
            events.append((r, h)) #離場
        events.sort()
        #Sweep
        result = []
        heap = [0]  # max-heap 用負數模擬，sentinel 0 確保 heap 不空
        removed = defaultdict(int) # lazy deletion 記錄
        prev_max = 0
        for x, h in events:
            if h < 0:
                heapq.heappush(heap, h) # 進場：把高度推進 heap（存負數）
            else:
                removed[h] += 1 # 離場：標記這個高度待刪除
            
            while heap and removed[-heap[0]] > 0: # 清掉 heap 頂端過期的
                removed[-heap[0]] -= 1
                heapq.heappop(heap)
                
            cur_max = -heap[0]
            if cur_max != prev_max:
                result.append([x, cur_max])
                prev_max = cur_max
        return result