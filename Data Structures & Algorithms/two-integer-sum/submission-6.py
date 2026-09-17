class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = {}

        ## build dict of nums and indx
        for i, num in enumerate(nums):
            ind[num] = i
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in ind and i != ind[diff]:
                return [i, ind[diff]]