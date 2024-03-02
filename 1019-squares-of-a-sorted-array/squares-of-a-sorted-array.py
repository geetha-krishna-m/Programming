class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        heap = []
        n = len(nums)
        for i in nums:
            heapq.heappush(heap,abs(i)**2)
        nums = []
        for i in range(n):
            nums.append(heapq.heappop(heap))
        return nums
        