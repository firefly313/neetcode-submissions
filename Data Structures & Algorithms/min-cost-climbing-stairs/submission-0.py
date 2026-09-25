class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        ## iterate through costs
        ## start at step 2, already cheapest cost to get there
        for i in range(2, n):
            ## add curr cost with the min of the previous
            cost[i] += min(cost[i-1], cost[i-2])

        ## return the min of the last two 
        ## stair costs
        return min(cost[n-1], cost[n-2])