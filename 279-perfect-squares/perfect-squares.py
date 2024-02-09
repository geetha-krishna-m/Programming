# class Solution:
#     def numSquares(self, n: int) -> int:
#         cache = [-1]*(n+1)
#         def solve(n):
#             if n == 0:
#                 return 0
#             if cache[n]!=-1:
#                 return cache[n]
#             mini,i = n,1
#             while i*i<=n:
#                 pSquare = i*i
#                 ans = 1 + solve(n-pSquare)
#                 mini = min(ans,mini)
#                 i += 1
#             cache[n] = mini
#             return mini
#         return solve(n)
class Solution:
    def numSquares(self, n: int) -> int:
        memo = [float('inf')] * (n + 1)
        memo[0] = 0
        
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                memo[i] = min(memo[i], 1 + memo[i - j * j])
                j += 1
                
        return memo[n]