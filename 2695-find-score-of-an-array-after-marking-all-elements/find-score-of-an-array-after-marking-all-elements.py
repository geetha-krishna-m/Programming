class Solution:
    def findScore(self, nums: List[int]) -> int:
        score, n = 0, len(nums)
        stack = [(nums[i],i) for i in range(n)]
        stack.sort(key = lambda x:x[0])
        visited = set()
        for i in range(n):
            ind = stack[i][1]
            if(ind not in visited):
                score = score + stack[i][0]
                visited.add(ind)
                if(ind-1>-1):
                    visited.add(ind-1)
                if(ind+1<n):
                    visited.add(ind+1)
        return score

