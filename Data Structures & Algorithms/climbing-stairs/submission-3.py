class Solution:
    def climbStairs(self, n: int) -> int:
        ## base base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
            
        dp = [0] * (n+1)

        ## base cases
        dp[1] = 1
        dp[2] = 2

        ## loop
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]