class Solution:
    def climbStairs(self, n: int) -> int:
        # Bottom - Up DP
        # if(n<=2):
        #     return n
        # else:
        #     dp = [0 for i in range(n+1)]
        #     dp[1],dp[2] = 1,2
        #     for i in range(3,n+1):
        #         dp[i] = dp[i-1]+dp[i-2]
        # return dp[n]
        memo = dict()
        def recursiveDP(n):
            if(n<=2):
                return n
            elif n in memo:
                return memo[n]
            else:
                memo[n] = recursiveDP(n-1)+recursiveDP(n-2)
                return memo[n]
        return recursiveDP(n)