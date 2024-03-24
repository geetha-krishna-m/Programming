from sortedcontainers import SortedList
class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        d = Counter()
        s = SortedList()
        ans = []
        for i in range(len(nums)):
            s.discard(d[nums[i]])
            d[nums[i]] += freq[i]
            s.add(d[nums[i]])
            ans.append(s[-1])
        return ans