class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            curr_idx = i
            while stack and h < stack[-1][1]:
                idx, height = stack.pop()
                width = i - idx
                maxArea = max(maxArea, width*height)
                curr_idx = idx
            stack.append((curr_idx, h))

        for idx, height in stack:
            width = len(heights) - idx
            maxArea = max(maxArea, width * height)
        
        return maxArea