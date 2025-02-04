class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maximum_sum,n,sums = nums[0],len(nums),nums[0]
        for i in range(1,n):
            if(nums[i-1]<nums[i]):
                sums += nums[i]
            else:
                sums = nums[i]
            maximum_sum = max(maximum_sum,sums)
        return maximum_sum

        