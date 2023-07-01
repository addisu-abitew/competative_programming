class Solution(object):
    def maxArea(self, height):
        l, r = 0, len(height)-1
        max_area = 0
        while r > l:
            h = min(height[l], height[r])
            w = r - l
            area = h * w
            
            max_area = max(area, max_area)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area