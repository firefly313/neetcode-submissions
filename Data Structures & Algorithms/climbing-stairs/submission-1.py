class Solution:
    def climbStairs(self, n: int) -> int:
        ## initialize array size
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * (n+1)
        ## base cases
        dp[1] = 1 ## 1
        dp[2] = 2 ## 1, 1 or 2
        ## loop goes from i = 3 to n+1
        for i in range(3, n+1):
            ## num of ways to reach with 1 step or 2 steps
            dp[i] = (dp[i-1] + dp[i-2])
        
        return dp[n]