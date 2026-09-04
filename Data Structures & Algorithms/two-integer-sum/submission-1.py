class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## hash map solution
        mydict = {}
        ans = []
        ## add all our indicies  to a dict
        for i, num in enumerate(nums):
            ## we want index to be the value for V
            mydict[num] = i
    
        for i, num in enumerate(nums):
            ## diff will be the other num we're looking for
            diff = target - num
            ## check if other num is there
            if diff in mydict and mydict[diff] != i:
                ## return both indicies
                return [i, mydict[diff]] 
        return ans
