class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        for i in range(n):
            res.append(nums[i])
            sums = nums[i]
            for j in range(i+1,n):
                sums += nums[j]
                res.append(sums)
        res.sort()
        return sum(res[left-1:right])%(10**9+7)
        