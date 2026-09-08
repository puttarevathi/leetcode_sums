class Solution(object):
    def maxArea(self, height):
            maximum = 0
            l  = 0
            r = len(height) - 1
            while l < r:
                area = min(height[l],height[r]) * (r - l)
                maximum = max(maximum, area)
                if height[l] < height[r]:
                    l += 1
                elif height[l] > height[r]:
                      r -= 1
                else:
                    l += 1
                    r -= 1
            return maximum      
