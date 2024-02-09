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
# class Solution:
#     def numSquares(self, n: int) -> int:
#         memo = [float('inf')] * (n + 1)
#         memo[0] = 0
        
#         for i in range(1, n + 1):
#             j = 1
#             while j * j <= i:
#                 memo[i] = min(memo[i], 1 + memo[i - j * j])
#                 j += 1
                
#         return memo[n]
class Solution:
    
    def numSquares(self, n: int) -> int:
        #using lagranges four-square theorem 
        def isSquare(n):
            if(math.ceil(n**0.5) == math.floor(n**0.5)):
                return True
            return False
        while(n%4 == 0):
            n = n//4
        if(n%8 == 7):
            return 4
        if(isSquare(n)):
            return 1
        i = 1
        while(i*i<=n):
            y = n - i*i
            if(isSquare(y)):
                return 2
            i += 1
        return 3
