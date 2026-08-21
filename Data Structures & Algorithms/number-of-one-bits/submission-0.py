class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = bin(n).count('1')
        return ans
        
        #res = 0
        #for i in range(32):
        ## left shift 1, check AND against n to see if its a 1, 
        ## if its 
        #    if (1 << i) & n:
        #        res += 1
        #return res