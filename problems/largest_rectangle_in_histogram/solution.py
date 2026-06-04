class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #存index
        max_area = 0
        heights = heights + [0]
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:  #stack=[] 跟 stack=None 都會跳過
                height = heights[stack.pop()]  #取出第一個左邊高度
                if stack:
                    left = stack[-1]
                else:
                    left = -1
                width = i - left - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area