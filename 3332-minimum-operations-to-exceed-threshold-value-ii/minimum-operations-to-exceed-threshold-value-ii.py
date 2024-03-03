import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        def check(nums,k):
            for x in nums:
                if x<k:
                    return False
            return True
        cnt = 0
        while(not check(nums,k)):
            print(cnt)
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            add = min(x,y)*2 + max(x,y)
            heapq.heappush(nums,add)
            cnt += 1
        return cnt
        