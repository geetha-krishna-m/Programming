class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i,n = 0,len(nums)
        if k == 0:
            return False
        k = n-1 if k > n-1 else k
        visited = set()
        for i in range(n):
            if i>k:
                visited.remove(nums[i-k-1])
            if nums[i] in visited:
                return True
            visited.add(nums[i])
        return False