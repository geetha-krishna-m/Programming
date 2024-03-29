class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        start,end,n = 0,0,len(nums)
        d = dict()
        
        while(end<n):
            d[nums[end]] = d.get(nums[end],0)+1 
            if(d[nums[end]]>k):
                d[nums[end]] -= 1
                break
            end += 1
        maxy = end - start
        print(maxy)
        while(end<n):
            d[nums[end]] = d.get(nums[end],0) + 1
            if(d[nums[end]] > k):
                while(d[nums[end]]>k and start<end):
                    d[nums[start]] -= 1
                    start += 1
                maxy = max(maxy,end-start+1)
            maxy = max(maxy,end-start+1)
            end = end + 1
        return maxy      