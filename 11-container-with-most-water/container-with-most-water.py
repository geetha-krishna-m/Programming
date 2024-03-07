class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        max_area = 0
        while i<j:
            side = min(height[i],height[j])
            max_area = max(max_area,side*(j-i))
            if(side == height[i]):
                i += 1
            else:
                j -= 1
        return max_area
        

        