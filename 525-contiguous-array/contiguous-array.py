class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counter = 0
        ans = 0
        hashmap = {}
        
        for i in range(len(nums)):
            
            if nums[i] == 1:
                counter += 1
            else:
                counter -= 1
                
            if counter == 0:
                size = i + 1
                ans = size
                
            elif counter in hashmap:
                size = i - hashmap[counter]
                if size > ans:
                    ans = size
                
            else:
                hashmap[counter] = i
            
        return ans
        