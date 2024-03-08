class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
        maxy = Counter(d.values())
        return maxy[max(d.values())]*max(d.values())

                
        
        
        