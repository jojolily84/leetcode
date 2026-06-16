class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #統計兩個 array 各自的頻率
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        result = []
        for num in count1:
            if num in count2:
                freq = min(count1[num], count2[num])
                result.extend([num] * freq) #extend:逐一加入每個 element
        return result

