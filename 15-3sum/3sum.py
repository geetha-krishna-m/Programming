class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort nums
        nums.sort()
        
        # Edge case 1
        if len(nums) < 3:
            return []
        
        # Initialize
        res = []
        
        # Iterate
        for i, num in enumerate(nums):
            # Sliding window
            l = i + 1
            r = len(nums) - 1
            
            # Eliminate calculating for same value
            if i > 0 and num == nums[i-1]:
                continue

            while l < r:
                curr_sum = num + nums[l] + nums[r]
                if curr_sum == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    # Eliminate calculating for same value
                    while l < r and nums[l]==nums[l-1]:
                        l += 1
                        
                elif curr_sum > 0:
                    r -= 1
                else:
                    l += 1
        return res