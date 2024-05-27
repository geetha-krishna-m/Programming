class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        i = 1
        tind = len(nums)
        while i<1001:
            ind = bisect.bisect_left(nums,i)
            if(tind-ind == i):
                return i
            i += 1
        return -1



        