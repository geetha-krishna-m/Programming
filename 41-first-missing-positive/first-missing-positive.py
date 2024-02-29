class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        index = 0
        N = len(nums)
        while index < N:
            temp = nums[index] - 1
            if nums[index] > 0 and nums[index] < N and nums[temp] != nums[index]:
                nums[index], nums[temp] = nums[temp], nums[index]
            else:
                index += 1

        print(nums)
        for i in range(N):
            if nums[i] != i + 1:
                return i + 1
        return N + 1