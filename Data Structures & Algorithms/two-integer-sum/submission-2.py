class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## create a dictionary
        indx = {}

        ## loop thro nums
        for i, num in enumerate(nums):
            indx[num] = i
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in indx and indx[diff] != i:
                return [i, indx[diff]]
        
        ## base case
        return []