import bisect
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = [0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                res[i] = (1 if nums[i]%2!=0 else 0)
            else:
                res[i] = res[i-1] + (1 if nums[i]%2!=0 else 0)
        count,req_k = 0,k
        for i in range(len(nums)):
            lind = bisect.bisect_left(res,req_k)
            rind = bisect.bisect_right(res,req_k)
            diff = rind - lind
            if(diff<=0):
                break
            count += rind-lind
            if nums[i]%2!=0:
                req_k += 1
        return count