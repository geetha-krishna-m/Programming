class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for i in nums:
            size = len(result)
            for j in range(size):
                subset = list(result[j])
                subset.append(i)
                result.append(subset)
        return result
        