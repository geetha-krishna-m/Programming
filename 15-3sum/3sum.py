class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        n,i = len(nums),0
        nums.sort()
        while(i<n):
            if(i>0 and nums[i] == nums[i-1]):
                i += 1
                continue
            j = i + 1
            k = n - 1
            while(j<k):
                sums = nums[i]+nums[j]+nums[k]
                if(sums == 0):
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while(j<n and nums[j]==nums[j-1]):
                        j += 1
                elif(sums > 0):
                    k -= 1
                else:
                    j += 1
            i = i + 1
        return res