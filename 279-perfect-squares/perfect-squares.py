class Solution:
    def numSquares(self, n: int) -> int:
        @cache
        def solve(n):
            if n == 0:
                return 0
            mini = float('inf')
            i = 1
            while i*i<=n:
                pSquare = i*i
                ans = 1 + solve(n-pSquare)
                mini = min(ans,mini)
                i += 1
            return mini
        return solve(n)