class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = list()
        n = len(nums)
        def permute(nums,index):
            if(index == n-1):
                result.append(list(nums))
                return
            for i in range(index,n):
                nums[i],nums[index] = nums[index],nums[i]
                permute(nums,index+1)
                nums[i],nums[index] = nums[index],nums[i]
        permute(nums,0)
        return result

