class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height)-1
        
        while left < right: # 왼쪽과 오른쪽이 만날때까지 반복
            h = min(height[left], height[right])
            w = right - left
            area = h*w

            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area