class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        res = [0 for i in range(n)]
        for i in range(1,n):
            res[i] = res[i-1] + (1 if(nums[i-1]%2 == nums[i]%2) else 0)
        final = []
        print(res)
        for i in queries:
            if(res[i[0]] == res[i[1]]):
                final.append(True)
            else:
                final.append(False)
        return final