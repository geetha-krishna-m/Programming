class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        prefixMap = {0:1}
        count  = 0
        for i in nums:
            prefixSum += i
            mod = prefixSum % k
            if mod<0:
                mod += k
            if mod in prefixMap:
                count += prefixMap[mod]
                prefixMap[mod] += 1
            else:
                prefixMap[mod] = 1
        return count
        