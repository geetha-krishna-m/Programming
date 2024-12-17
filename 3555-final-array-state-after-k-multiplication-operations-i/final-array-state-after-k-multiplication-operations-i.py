class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        dup_list = [(num,i) for i,num in enumerate(nums)]
        heapify(dup_list)
        for i in range(k):
            val,i = heappop(dup_list)
            nums[i] = (val)*multiplier
            heappush(dup_list,(nums[i],i))
        return nums

        