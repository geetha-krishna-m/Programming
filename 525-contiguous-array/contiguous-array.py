class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        sum_index = {0:-1}
        curr_sum = 0
        ans = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                curr_sum += -1
            elif nums[i] == 1:
                curr_sum += 1

            if curr_sum in sum_index:
                max_len = (i - sum_index[curr_sum])
                if max_len > ans:
                    ans = max_len
            else:
                sum_index[curr_sum] = i
        return ans



        