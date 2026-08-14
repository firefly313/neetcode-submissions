class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## select lowest number
        ## then select highest number after it
        ## as long as it is higher than lowest
        ## formula profit = highest - lowest

        ## no profit if it decreases the whole time
        for i in range(len(prices)-1):
            if prices[i] <= prices[i+1]:
                break
            else:
                if i == len(prices) - 2:
                    return 0
                continue

        lowest = prices[0]
        profit = 0
        best = 0
        for i in range(1, len(prices)):
            curr = prices[i]
            if curr < lowest:
                lowest = curr
            profit = curr - lowest
            if profit > best:
                best = profit
        return best

        

        ## must be profitable somewhere
        ## get lowest, keep track of index
        ## find highest after lowest
        #lowest = 101
        #lowest_index = -1
        #profit = 0
        #for i in range(len(prices)):
        #    curr = prices[i]
        #    if curr < lowest:
                #lowest = curr
                #lowest_index = i
        
        #highest = -1
        #for i in range(lowest_index, len(prices)):
        #    curr = prices[i]
        #    if curr > highest:
        #        highest = curr
        
        #profit = highest - lowest
        #if profit < 0:
        #    return 0
        #return profit
            
