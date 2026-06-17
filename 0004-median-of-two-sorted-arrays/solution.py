class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 確保對較短的 array 做 binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2  #m+n+1:讓左半部在奇數時多一個元素
        
        lo, hi = 0, m #搜尋切點，可能全都在左邊，所以範圍是0~m.
        while lo <= hi:
            i = (lo + hi) // 2 # nums1 的切點
            j = half - i       # nums2 的切點
            # 切點邊界處理：用 -inf / +inf 避免 index out of range
            L1 = nums1[i - 1] if i > 0 else float('-inf')
            R1 = nums1[i]     if i < m else float('inf')
            L2 = nums2[j - 1] if j > 0 else float('-inf')
            R2 = nums2[j]     if j < n else float('inf')
            
            if L1 <= R2 and L2 <= R1:
                if (m + n) % 2 == 1:
                    return float(max(L1, L2))
                else:
                    return (max(L1,L2) + min(R1, R2)) / 2.0 #Python 3 中 / 永遠回傳 float，不需要額外轉型。
            elif L1 > R2:
                hi = i - 1 # i 太大，往左縮
            else:
                lo = i + 1 # i 太小，往右擴
