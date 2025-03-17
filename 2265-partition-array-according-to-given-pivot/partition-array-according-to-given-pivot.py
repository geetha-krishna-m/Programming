class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        i,j = 0,n-1
        res = [0 for i in range(n)]
        for k in range(n):
            if(nums[k]<pivot):
                res[i] = nums[k]
                i = i + 1
            if(nums[n-k-1]>pivot):
                res[j] = nums[n-k-1]
                j = j - 1
        for m in range(i,j+1):
            res[m] = pivot
        return res


        