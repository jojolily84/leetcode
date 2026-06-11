class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        return [num for num, freq in Counter(nums).most_common(k)]
        """
        freq_map = Counter(nums) #nums = [1,1,1,2,2,3]->{1:3, 2:2, 3:1}
        buckets = [[] for _ in range(len(nums) + 1)] # index 代表頻率，長度 n+1 確保 freq=n 時不越界

        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        result = []
        for freq in range(len(buckets)-1, 0, -1): # 從高頻到低頻
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
